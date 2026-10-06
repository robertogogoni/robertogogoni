# Local profile metrics

The profile SVGs are rendered locally with the official `lowlighter/metrics`
container and published with Git. This bypasses GitHub Actions. The renderer
reads the three configurations in `metrics-config.yml`.

## Requirements

- Rootless Podman and the `gh` CLI, signed in as `robertogogoni`.
- Python 3 with PyYAML (`python -c 'import yaml'`).
- A clean checkout at `~/Work/robertogogoni` for automatic publishing.
- Network access to GitHub and GitHub Container Registry.

The script asks `gh` for its existing token at run time. It passes the token to
the container through a private temporary environment file, removes that file
after rendering, and never writes the token to the repository. The container
needs the token to query GitHub; use a narrowly scoped token when available.

## Run manually

```bash
podman pull ghcr.io/lowlighter/metrics:latest
python scripts/refresh_metrics_local.py
git diff --stat -- metrics*.svg
```

The manual command renders all five SVGs into the checkout for review. To commit
and push automatically from a clean checkout:

```bash
python scripts/refresh_metrics_local.py --publish
```

Rendering validates every SVG before replacing any existing file. Publication
stages only the three metrics SVGs and uses a normal fast-forward pull and push.
If the checkout has other changes or the remote moves during rendering, the
script stops without forcing a push.

## Install the local timer

```bash
mkdir -p ~/.config/systemd/user
cp systemd/profile-metrics-refresh.service ~/.config/systemd/user/
cp systemd/profile-metrics-refresh.timer ~/.config/systemd/user/
systemctl --user daemon-reload
systemctl --user enable --now profile-metrics-refresh.timer
systemctl --user list-timers profile-metrics-refresh.timer
```

It runs daily between 03:00 and 04:00 local time and catches up after a missed
run. Check results with `systemctl --user status profile-metrics-refresh.service`
or `journalctl --user -u profile-metrics-refresh.service`. A user timer runs only
while the user manager is active; enable lingering if updates must run while
logged out and the host stays powered on.

The previous GitHub metrics workflow was removed after its settings were moved
to `metrics-config.yml`. The unused README cache-busting and snake workflows
were also removed. Their scheduled runs were blocked by a GitHub account
billing restriction; the local timer does not use GitHub Actions.

The upstream habits and recent-activity plugins currently fail on some GitHub
event payloads and emit SVGs containing `Unexpected error`. They are excluded
from the local configuration until that bug is fixed. The script rejects error
SVGs rather than publishing them.
