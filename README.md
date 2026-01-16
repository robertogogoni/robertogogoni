# Hi, I'm Roberto

I build tools that solve real problems.

---

## Featured Project

### [update-beeper](https://github.com/robertogogoni/update-beeper)

A self-healing Beeper Desktop updater for Arch Linux.

```
  Self-healing updates     Automatic rollback     Always latest
         |                       |                      |
    Retries with            Restores previous      Bypass AUR
    targeted fixes          version on failure     delays
```

**Why it exists:** Beeper's built-in updater doesn't work on Arch Linux—updates download but can't overwrite pacman-managed files. The AUR package is always days behind. This script downloads directly from Beeper's API with automatic recovery and rollback.

[![Lint](https://github.com/robertogogoni/update-beeper/actions/workflows/lint.yml/badge.svg)](https://github.com/robertogogoni/update-beeper/actions/workflows/lint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

```bash
# Quick install
curl -fsSL https://raw.githubusercontent.com/robertogogoni/update-beeper/main/install.sh | bash
```

---

<sub>Building practical solutions for everyday problems</sub>
