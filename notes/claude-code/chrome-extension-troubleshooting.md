# Claude in Chrome Extension Troubleshooting

> Session date: 2026-01-21

## Issue: "Chrome extension is not detected" at startup

### Symptom
Every time Claude Code starts, it shows "Chrome extension is not detected" even though the extension is installed and working.

### Root Cause
Stale cache value in `~/.claude.json`:
```json
"cachedChromeExtensionInstalled": false
```

### Fix
Edit `~/.claude.json` and change:
```json
"cachedChromeExtensionInstalled": true
```

### Why it happens
Claude Code caches extension detection to speed up startup. This cache can become stale after:
- Extension updates
- Claude Code updates
- Manual extension reinstalls

### Verification
After the fix, restart Claude Code - the warning should be gone.

---

## Bug Found: Navigate tool corrupts special URL schemes

### Issue
The `mcp__claude-in-chrome__navigate` tool incorrectly handles special browser URL schemes.

### Examples
| Input | Expected | Actual |
|-------|----------|--------|
| `chrome://extensions` | `chrome://extensions` | `https://chrome//extensions` |
| `about:blank` | Navigate to blank | "Invalid URL" error |

### Root Cause
The tool defaults to prepending `https://` when no protocol is detected, but it doesn't recognize `chrome://`, `about:`, `file://`, etc. as valid protocols.

### Bug Report Filed
- **GitHub Issue:** https://github.com/anthropics/claude-code/issues/19911
- **Status:** Open

---

## Environment Reference

### Chrome Canary Native Messaging Setup

**Native messaging host location:**
```
~/.config/google-chrome-canary/NativeMessagingHosts/com.anthropic.claude_code_browser_extension.json
```

**Host configuration:**
```json
{
  "name": "com.anthropic.claude_code_browser_extension",
  "description": "Claude Code Browser Extension Native Host",
  "path": "/home/rob/.claude/chrome/chrome-native-host",
  "type": "stdio",
  "allowed_origins": [
    "chrome-extension://fcoeoabgfenejglbffodgkkbkcdhcgfn/"
  ]
}
```

**Native host script:** `~/.claude/chrome/chrome-native-host`
```sh
#!/bin/sh
exec "/home/rob/.local/share/claude/versions/X.X.X" --chrome-native-host
```
(Version number updates with Claude Code updates)

### Extension ID
- **Claude Extension:** `fcoeoabgfenejglbffodgkkbkcdhcgfn`

### Key Files
| File | Purpose |
|------|---------|
| `~/.claude.json` | Claude Code global config, includes extension cache |
| `~/.claude/chrome/chrome-native-host` | Native messaging bridge script |
| `~/.config/google-chrome-canary/Default/Preferences` | Chrome extension states |

---

## Useful Commands

```bash
# Check if extension is installed
ls ~/.config/google-chrome-canary/Default/Extensions/fcoeoabgfenejglbffodgkkbkcdhcgfn/

# Check native messaging config
cat ~/.config/google-chrome-canary/NativeMessagingHosts/com.anthropic.claude_code_browser_extension.json

# Check Claude Code version
claude --version

# Check extension version
grep '"version"' ~/.config/google-chrome-canary/Default/Extensions/fcoeoabgfenejglbffodgkkbkcdhcgfn/*/manifest.json
```
