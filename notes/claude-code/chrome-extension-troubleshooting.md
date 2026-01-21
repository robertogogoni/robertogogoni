# Claude in Chrome Extension Troubleshooting

> Session date: 2026-01-21

---

## Claude Code Chrome CLI Flags

```bash
# Enable Chrome integration (default if extension detected)
claude --chrome

# Disable Chrome integration
claude --no-chrome
```

---

## Key Settings in ~/.claude.json

```json
{
  "claudeInChromeDefaultEnabled": true,        // Chrome integration enabled
  "hasCompletedClaudeInChromeOnboarding": true, // Onboarding completed
  "cachedChromeExtensionInstalled": true        // Extension detection cache (THE FIX)
}
```

---

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

## Multi-Browser Consideration

The Claude extension might be installed in only ONE browser, but native messaging hosts get configured in ALL browsers:

| Browser | Native Host Configured | Extension Installed |
|---------|----------------------|---------------------|
| Chrome Canary | ✅ `~/.config/google-chrome-canary/NativeMessagingHosts/` | ✅ Yes |
| Chrome | ✅ `~/.config/google-chrome/NativeMessagingHosts/` | ❌ No |
| Chromium | ✅ `~/.config/chromium/NativeMessagingHosts/` | ❌ No |

**Important:** If Claude Code reports "extension not detected", verify the extension is actually installed in the browser you're using, not just that the native host is configured.

### Check extension presence in all browsers:
```bash
for browser in google-chrome google-chrome-canary chromium; do
  ext_dir="$HOME/.config/$browser/Default/Extensions/fcoeoabgfenejglbffodgkkbkcdhcgfn"
  if [ -d "$ext_dir" ]; then
    echo "✅ $browser: Extension installed"
  else
    echo "❌ $browser: Extension NOT installed"
  fi
done
```

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

# Check MCP socket exists
ls -la /tmp/claude-mcp-browser-bridge-$USER

# Check if chrome-in-chrome MCP is running
ps aux | grep "claude-in-chrome-mcp"

# Test native host directly
timeout 2 ~/.claude/chrome/chrome-native-host 2>&1 || true
```

---

## Chrome Enterprise Policies (Related - from past session 2026-01-05)

If using Chrome policies for content blocking, be aware of policy precedence:

### Policy file locations
```
/etc/opt/chrome/policies/managed/           # Regular Chrome
/etc/opt/google/chrome-canary/policies/managed/  # Chrome Canary
```

### Common issue: Policies being "superseded"
When multiple policy files set the same key, Chrome may show:
```
DefaultPopupsSetting: 1
  ⚠️ SUPERSEDED by: [{'level': 'mandatory', 'scope': 'machine', 'source': 'platform', 'value': 1}]
```

**Solution:** Ensure only ONE policy file sets each key, or use the same value across all files.

### Verify loaded policies
1. Navigate to `chrome://policy`
2. Click "Export policies" to download JSON
3. Check for `superseded` warnings in the export

### Export policies via CLI
```bash
# Chrome must be running
# Export is done through chrome://policy UI
```
