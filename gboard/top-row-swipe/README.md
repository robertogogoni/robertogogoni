# Gboard Top-Row-Swipe — custom slot sets

Ready-to-import configuration files for the **Swipeable Custom Top Row** patch
from [jasonwu1994/Gboard-patches](https://github.com/jasonwu1994/Gboard-patches).

That patch lets you swipe the keyboard's top row horizontally to reveal **10
customizable slots**. Each slot either commits a fixed piece of text or runs a
sandboxed JavaScript snippet (via an embedded QuickJS engine) and commits
whatever the script returns.

## ⚠️ Security note before you import anything

If you exported your own config that contained an OpenAI key, treat that key as
**compromised** — an exported `.json` stores the key in plaintext. Rotate it at
<https://platform.openai.com/api-keys> and never share an export with the key
filled in. The `04-ai-writing-tools` file here ships with a **placeholder**;
you paste your key locally, on-device, after importing.

## The files

| File | Needs network? | Needs API key? | What it gives you |
|------|:--:|:--:|---|
| `01-text-productivity.slots.json` | No | No | Symbols + text transforms: UPPER/lower/Title case, whitespace cleanup, reverse, insert today's date |
| `02-emoji-kaomoji.slots.json` | No | No | Table-flip and friends, plus common symbols (★ ♥ ✓ ✗ •) |
| `03-dev-utilities.slots.json` | No | No | JSON pretty/minify, URL & Base64 encode, JSON-string-escape, slugify, UUIDv4, unix/ISO timestamps |
| `04-ai-writing-tools.slots.json` | Yes | **Yes** (yours) | Improve, fix grammar, summarize, translate (EN/ES), formalize, shorten, bulletize, reply, emojify |
| `05-web-utilities.slots.json` | Yes | No (free public APIs) | Public IP, weather, USD FX rates, dictionary, GitHub user lookup, UTC clock, dice/coin, word/char count |

## How to import

Verified against build **Patch Version 2.0.0-dev.4** (Gboard Patches 1.14.0 /
Morphe Patches 1.35.0), package `dev.jason.com.google.android.inputmethod.latin`.

1. Open the patched Gboard's **Patch settings → Features → Keyboard → Custom
   Top Row**.
2. Under **TRANSFER**, tap **Import settings** and pick one of the
   `*.slots.json` files. This replaces Global JavaScript, runtime limits, and
   **all 10 slots** at once. (**Reset slots** under ADVANCED restores the default
   emoji row.)
3. For `04-ai-writing-tools`, open **Global JavaScript** and replace
   `PUT_YOUR_OPENAI_API_KEY_HERE` with your real key (and change `OPENAI_MODEL`
   if you like).
4. On the keyboard, **swipe the top row horizontally** to switch from the stock
   row to your custom row, then **tap a slot** to fire it — each tap starts a
   fresh QuickJS runtime. For transform/AI slots, **select the target text
   first**; it arrives in the script as `input`.

Each file replaces all 10 slots at once, so import the set that fits the
context. You can also mix-and-match by hand-editing a file before importing.

> **Note on commits:** a slot only commits when its script returns a non-null
> value, and the commit is **skipped if the input field changed during
> execution**. For slow network/AI slots that's expected — don't tap away or
> switch fields while it's working.

## File format reference

Confirmed against the patch source (`GboardTopRowSwipeSettings.java`,
`GboardQuickJsFeature.java`).

```jsonc
{
  "format": "gboardpatches.top-row-swipe.slots",  // required, must match exactly
  "version": 3,                                     // required, 1 or 3 accepted
  "globalJavaScript": "…",                          // optional: runs before every slot
  "javaScriptRuntimeLimits": {                      // optional: sandbox ceilings
    "responseBodyLimitBytes": 1048576,              //   default 1 MB
    "timeoutMaxMs": 30000,                          //   default 30 s (per-slot ceiling)
    "memoryLimitBytes": 8388608,                    //   default 8 MB
    "maxStackBytes": 524288                         //   default 512 KB
  },
  "slots": [ /* exactly 10 objects */
    {
      "displayText": "AA",   // required, non-blank — the label on the swipe strip
      "commitText": "",      // text committed when isJavaScript is false
      "isJavaScript": true,  // true → run scriptText instead of committing commitText
      "scriptText": "return String(input || '').toUpperCase();",
      "timeoutMs": 1500      // per-slot execution budget, ≤ timeoutMaxMs
    }
    // …9 more
  ]
}
```

### The JavaScript runtime (QuickJS sandbox)

- **`input`** — a string: the currently selected text (empty if nothing is
  selected). Your script's job is usually to transform `input`.
- **Return value** — whatever you `return` is coerced with `String(value)` and
  committed. Return `null`/`undefined` to commit nothing.
- **Execution model** — `globalJavaScript` runs first (define shared consts and
  helper functions there), then the slot body runs as a function of `input`.
- **`httpRequest({ method, url, headers, body })`** — performs an HTTP request
  and returns the **response body as a string**. Parse JSON yourself with
  `JSON.parse(...)`. Used by the AI set because it needs an `Authorization`
  header.
- **`httpGet(url)`** — convenience GET that returns the body string. Used by
  `05-web-utilities` (wrapped in a `GET()` helper as a harmless fallback).
- **`httpPost(url, body)`** — convenience POST that returns the body string, for
  simple posts that don't need custom headers.

The patch's own in-app **JavaScript Guide** lists the host extras as: `input`,
`httpRequest(options)`, `httpGet(url)`, and `httpPost(url, body)`.
- Standard ECMAScript is available: `JSON`, `Math`, `Date`, `String`/`Array`
  methods, `encodeURIComponent` / `decodeURIComponent`, regexes. Browser-only
  globals (`btoa`, `fetch`, `document`, `localStorage`) are **not** — that's why
  `03-dev-utilities` ships a pure-JS Base64 implementation.
- Limits: scripts are capped by `timeoutMs`, memory, stack, and response-body
  size. Keep network slots fast and defensive (`try/catch`, offline fallbacks).

## More enhancement ideas (easy to add yourself)

**Offline / text (no key, instant):**
- **Lorem ipsum** generator for form testing.
- **ROT13 / Caesar** obfuscation.
- **Case cycler**: detect current case of `input` and rotate UPPER → Title → lower.
- **Smart quotes**: convert `"straight"` to `"curly"` quotes and `--` to `—`.
- **Markdown → plain**: strip `*`, `#`, backticks for pasting into plain fields.
- **Sum / average** the numbers found in the selection.
- **Currency/number formatting** with thousands separators.
- **Diacritics stripper** (`café` → `cafe`) for slugs and search.

**Networked, key-less public APIs:**
- **URL shortener/expander**, **QR text**, **crypto price** (CoinGecko),
  **random joke/quote**, **timezone lookup**, **country info** (restcountries),
  **package version** (npm/PyPI registry), **HTTP status** of a URL you selected.

**AI-powered (reuse the `ai()` helper pattern):**
- **Explain / define like I'm 5** the selection.
- **Translate to N languages** at once, or **auto-detect → your language**.
- **Tone presets**: friendly / assertive / apologetic / concise.
- **Extract action items** or **turn notes into an email**.
- **Code explain / add comments** for a selected snippet.
- Swap the backend to **Anthropic** (`https://api.anthropic.com/v1/messages`,
  `x-api-key` + `anthropic-version` headers, read `content[0].text`) or to a
  **local LLM** on your LAN — only the `ai()` helper changes; slots stay the same.

**Config/architecture tips:**
- Put **all shared secrets and helpers in `globalJavaScript`** so a slot body is
  a one-liner — easier to read and to re-point at a different provider.
- Keep **provider-specific sets in separate files** (OpenAI set, Anthropic set,
  offline set) and import whichever you're using.
- Because an export embeds secrets in plaintext, **keep a key-less "shareable"
  copy** of any set you plan to publish, and a separate on-device copy with the
  key filled in.
