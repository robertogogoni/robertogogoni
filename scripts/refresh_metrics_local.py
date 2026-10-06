#!/usr/bin/env python3
"""Render the profile's lowlighter metrics locally, without GitHub Actions."""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import xml.etree.ElementTree as ET

import yaml


REPO = Path(__file__).resolve().parents[1]
CONFIG = REPO / "metrics-config.yml"
IMAGE = "ghcr.io/lowlighter/metrics:latest"
EXPECTED_FILES = {
    "metrics.svg",
    "metrics-languages.svg",
    "metrics-isocalendar.svg",
}


def run(command, *, capture=False, timeout=None):
    return subprocess.run(
        command,
        cwd=REPO,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.STDOUT if capture else None,
        timeout=timeout,
    )


def read_jobs():
    steps = yaml.safe_load(CONFIG.read_text())["metrics"]
    jobs = []
    for step in steps:
        options = dict(step["with"])
        filename = options.get("filename")
        if filename not in EXPECTED_FILES:
            raise ValueError(f"Unexpected metrics filename: {filename!r}")
        options.pop("token", None)
        jobs.append((filename, options))
    if {filename for filename, _ in jobs} != EXPECTED_FILES or len(jobs) != len(EXPECTED_FILES):
        raise ValueError("Metrics configuration outputs differ from expected files")
    return jobs


def read_token():
    token = run(["gh", "auth", "token"], capture=True).stdout.strip()
    if not token or "\n" in token:
        raise ValueError("GitHub CLI did not provide a usable token")
    return token


def env_value(value):
    if isinstance(value, bool):
        return "yes" if value else "no"
    return "" if value is None else str(value)


def write_env_file(path, token, options):
    values = {"INPUT_TOKEN": token, "INPUT_OUTPUT_ACTION": "none"}
    for key, value in options.items():
        values[f"INPUT_{key.upper()}"] = env_value(value)
    if any("\n" in value or "\r" in value for value in values.values()):
        raise ValueError("Multiline metrics options are not supported")
    path.write_text("".join(f"{key}={value}\n" for key, value in values.items()))
    path.chmod(0o600)


def validate_svg(path):
    if not path.is_file() or path.stat().st_size < 1000:
        raise ValueError(f"Missing or unexpectedly small SVG: {path.name}")
    root = ET.parse(path).getroot()
    if root.tag.rsplit("}", 1)[-1] != "svg":
        raise ValueError(f"Not an SVG: {path.name}")
    content = path.read_text(errors="replace")
    if "Something went wrong" in content or 'class="field error"' in content:
        raise ValueError(f"Renderer returned an error SVG: {path.name}")


def render(jobs, token, directory):
    image_present = subprocess.run(
        ["podman", "image", "exists", IMAGE], cwd=REPO, stdout=subprocess.DEVNULL
    ).returncode == 0
    if not image_present:
        run(["podman", "pull", IMAGE])
    env_file = directory / "metrics.env"
    for filename, options in jobs:
        write_env_file(env_file, token, options)
        print(f"Rendering {filename}...", flush=True)
        command = [
            "podman", "run", "--rm", "--pull=never",
            "--env-file", str(env_file),
            "--volume", f"{directory}:/renders:Z",
            IMAGE,
        ]
        try:
            result = run(command, capture=True, timeout=1200)
        except subprocess.CalledProcessError as error:
            output = (error.stdout or "").replace(token, "[redacted]")
            raise RuntimeError(f"Renderer failed for {filename}:\n{output[-4000:]}") from error
        try:
            validate_svg(directory / filename)
        except ValueError as error:
            output = (result.stdout or "").replace(token, "[redacted]")
            raise RuntimeError(f"{error}\nRenderer log:\n{output[-4000:]}") from error
        print(f"Rendered {filename} ({(directory / filename).stat().st_size} bytes)", flush=True)
    env_file.unlink()


def install_outputs(directory):
    for filename in sorted(EXPECTED_FILES):
        source = directory / filename
        staged = REPO / f".{filename}.new"
        shutil.copyfile(source, staged)
        os.replace(staged, REPO / filename)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--publish", action="store_true", help="Commit and push changed SVGs")
    args = parser.parse_args()

    if args.publish:
        if run(["git", "branch", "--show-current"], capture=True).stdout.strip() != "main":
            raise RuntimeError("Publishing requires the main branch")
        if run(["git", "status", "--porcelain"], capture=True).stdout.strip():
            raise RuntimeError("Publishing requires a clean checkout")
        run(["git", "pull", "--ff-only", "origin", "main"])

    jobs = read_jobs()
    token = read_token()
    with tempfile.TemporaryDirectory(prefix="profile-metrics-", dir=REPO) as temp:
        directory = Path(temp)
        render(jobs, token, directory)
        install_outputs(directory)

    if args.publish:
        run(["git", "add", "--", *sorted(EXPECTED_FILES)])
        changed = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=REPO)
        if changed.returncode == 0:
            print("Metrics are unchanged; nothing to publish")
            return
        if changed.returncode != 1:
            raise RuntimeError("Could not inspect staged metrics")
        run(["git", "commit", "-m", "metrics: refresh profile SVGs"])
        run(["git", "push", "origin", "main"])
        print("Published refreshed metrics")
    else:
        print("Refreshed metrics in checkout; review and commit when ready")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as error:
        print(f"metrics refresh failed: {error}", file=sys.stderr)
        sys.exit(1)
