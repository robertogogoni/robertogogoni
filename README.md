<p align="center">
  <a href="https://github.com/robertogogoni">
    <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=70A5FD&center=true&vCenter=true&random=false&width=600&lines=Hi%2C+I'm+Roberto+%F0%9F%91%8B;Scrum+Master+who+codes;Building+practical+solutions;Creator+of+Cortex" alt="Typing SVG" />
  </a>
</p>

Scrum Master who codes on the side. If something's broken or tedious, I'll probably write a script for it.

Sao Paulo, Brazil

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/robertogogoni)
[![X](https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/ragogoni)

---

## Tech Stack

![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![Arch Linux](https://img.shields.io/badge/Arch_Linux-1793D1?style=for-the-badge&logo=archlinux&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)

---

## Featured Project

### [Cortex](https://github.com/robertogogoni/cortex-claude)

**Claude's Cognitive Layer** - A dual-model memory system with auto-extraction, auto-recall, vector search, MCP tools for deep reasoning, and compounding learnings.

```
                         +---------------------------+
                         |    Claude Code Session    |
                         +-------------+-------------+
                                       |
            +==========================|==========================+
            |                   CORTEX MCP SERVER                 |
            +=====================================================+
            |                                                     |
            |   +------------------+     +-------------------+    |
            |   |   HAIKU WORKER   |     |  SONNET THINKER   |    |
            |   |                  |     |                   |    |
            |   |  o query         |     |  * reflect        |    |
            |   |  o recall        |     |  * infer          |    |
            |   |                  |     |  * learn          |    |
            |   |  ~$0.25/1M [fast]|     |  * consolidate    |    |
            |   +--------+---------+     |  ~$3/1M tokens    |    |
            |            |               +--------+----------+    |
            |            +--------+------+--------+               |
            |                     |                               |
            |   +-----------------v-----------------------+       |
            |   |        VECTOR SEARCH ENGINE             |       |
            |   |   HNSW Index + BM25 + RRF Fusion        |       |
            |   |   Local Embeddings (all-MiniLM-L6)      |       |
            |   +-----------------------------------------+       |
            |                                                     |
            +=====================================================+
                          |                       |
            +-------------+----------+  +---------+-------------+
            |     SESSION START      |  |      SESSION END      |
            |------------------------|  |-----------------------|
            |  - Context Analyzer    |  |  - Extraction Engine  |
            |  - Query Orchestrator  |  |  - Pattern Tracker    |
            |  - Memory Injection    |  |  - Outcome Scorer     |
            +------------------------+  +-----------------------+
                          |                       |
                          +-----------+-----------+
                                      |
            +-------------------------v-------------------------+
            |               LADS SELF-IMPROVEMENT               |
            |     Learnable | Adaptive | Documenting | Self-I   |
            +---------------------------------------------------+
```

| Problem | Cortex Solution |
|---------|-----------------|
| Claude forgets context | **Auto-recall**: Injects relevant memories at session start |
| Learnings are lost | **Auto-extraction**: Captures insights from every session |
| No semantic search | **Vector Search**: HNSW + BM25 hybrid with RRF fusion |
| No deep reasoning tools | **MCP Server**: 6 tools for query, recall, reflect, infer, learn, consolidate |
| Expensive API calls | **Dual-model**: Haiku for fast ops, Sonnet for deep reasoning |
| Manual memory management | **Fully automatic**: Zero user intervention required |

**NEW: `/cortex` Skill** - User-friendly slash commands:

```bash
/cortex              # Status overview
/cortex help         # All commands with examples
/cortex query "X"    # Search memories (~$0.001)
/cortex learn "X"    # Store insight (~$0.01)
/cortex reflect "X"  # Deep analysis (~$0.01)
/cortex stats        # Memory counts & API costs
/cortex health       # System health check
/cortex export       # Export memories (json/md)
```

[![Tests](https://img.shields.io/badge/tests-142%2F142%20passing-brightgreen)](https://github.com/robertogogoni/cortex-claude)
[![Node.js](https://img.shields.io/badge/node-%3E%3D18.0.0-blue)](https://github.com/robertogogoni/cortex-claude)
[![MCP](https://img.shields.io/badge/MCP-6%20tools-purple)](https://github.com/robertogogoni/cortex-claude)
[![Vector Search](https://img.shields.io/badge/vector-HNSW%20%2B%20BM25-orange)](https://github.com/robertogogoni/cortex-claude)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/robertogogoni/cortex-claude/blob/main/LICENSE)
[![Roadmap](https://img.shields.io/badge/roadmap-view-blueviolet)](https://github.com/robertogogoni/cortex-claude/blob/master/ROADMAP.md)

```bash
# One-command install
git clone https://github.com/robertogogoni/cortex-claude.git ~/.claude/memory
cd ~/.claude/memory && npm install
```

---

## Other Projects

### [claude-cross-machine-sync](https://github.com/robertogogoni/claude-cross-machine-sync)

AI-powered configuration sync across Windows & Linux machines with Claude Code. Auto-categorizes config changes (machine-specific vs platform vs universal), syncs via git with intelligent commit tags, and maintains searchable AI memory across all machines.

### [update-beeper](https://github.com/robertogogoni/update-beeper)

A self-healing Beeper Desktop updater for Arch Linux. Downloads directly from Beeper's API with automatic recovery and rollback.

[![Lint](https://github.com/robertogogoni/update-beeper/actions/workflows/lint.yml/badge.svg)](https://github.com/robertogogoni/update-beeper/actions/workflows/lint.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## GitHub Stats

<!-- STATS_UPDATED: 2026-02-02T07:27:08Z -->

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=robertogogoni&style=for-the-badge&color=1a1b27&label=PROFILE+VIEWS" alt="Profile Views"/>
</p>

### Trophies

<p align="center">
  <a href="https://github.com/ryo-ma/github-profile-trophy">
    <img src="https://github-profile-trophy.vercel.app/?username=robertogogoni&theme=tokyonight&no-frame=true&no-bg=true&column=7&margin-w=10" alt="GitHub Trophies"/>
  </a>
</p>

### Overview

<p align="center">
  <img src="https://github-readme-stats-zeta-blush-29.vercel.app/api?username=robertogogoni&show_icons=true&theme=tokyonight&hide_border=true&count_private=true&include_all_commits=true&show=reviews,prs_merged,prs_merged_percentage&v=20260202b" alt="GitHub Stats" height="180"/>
  <img src="https://github-readme-stats-zeta-blush-29.vercel.app/api/top-langs/?username=robertogogoni&layout=compact&theme=tokyonight&hide_border=true&langs_count=8&hide=Jupyter%20Notebook,HTML,CSS,Batchfile,Makefile&exclude_repo=hosts,adfilt,fuckfuckadblock,Adobe-URL-Block-List,Krakatau,developer-roadmap,awesome-oss-alternatives,awesome-shizuku,XClipper,apkscan,cookbook,Public-Guide&v=20260202b" alt="Top Languages" height="180"/>
</p>

### Streak

<p align="center">
  <img src="https://github-readme-streak-stats-eight.vercel.app?user=robertogogoni&theme=tokyonight&hide_border=true&date_format=j%20M%5B%20Y%5D" alt="GitHub Streak"/>
</p>

### Activity

<p align="center">
  <img src="https://github-readme-activity-graph-sage.vercel.app/graph?username=robertogogoni&theme=tokyo-night&hide_border=true&area=true&custom_title=Contribution%20Graph" alt="Activity Graph"/>
</p>

### Contributions

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/robertogogoni/robertogogoni/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/robertogogoni/robertogogoni/output/github-snake.svg">
  <img alt="github contribution grid snake animation" src="https://raw.githubusercontent.com/robertogogoni/robertogogoni/output/github-snake.svg">
</picture>

### Summary Cards

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=robertogogoni&theme=tokyonight" alt="Profile Details"/>
</p>

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=robertogogoni&theme=tokyonight" alt="Repos per Language" height="180"/>
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=robertogogoni&theme=tokyonight" alt="Most Commit Language" height="180"/>
</p>

<p align="center">
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/stats?username=robertogogoni&theme=tokyonight" alt="Stats Card" height="180"/>
  <img src="https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=robertogogoni&theme=tokyonight&utcOffset=-3" alt="Productive Time" height="180"/>
</p>

---

## Notes & Documentation

Personal troubleshooting guides and learnings.

| Topic | Description |
|-------|-------------|
| [Claude in Chrome Troubleshooting](notes/claude-code/chrome-extension-troubleshooting.md) | Fixes for extension detection issues, native messaging setup, and [bug #19911](https://github.com/anthropics/claude-code/issues/19911) |

---

<p align="center">
  <sub>Building practical solutions for everyday problems</sub>
</p>
