# DailyNote Patterns Reference

This document describes the observed structure and conventions of the user's DailyNote system in Obsidian.

## Directory Structure

```
DailyNote/
└── {YYYY}/                        # one directory per year
    ├── {YYYY} 想法汇总.md          # yearly summary (required)
    ├── {YYYY-MM-DD}.md             # standalone entries (optional, as needed)
    └── img/                        # images (optional)
```

Each year has a single summary file named `{YYYY} 想法汇总.md` and optional standalone day files. When a new year starts and the directory or summary file doesn't exist yet, create them following this convention.

> **Historical note**: 2024 and earlier used different naming (`汇总.md` / `简短想法.md`). Ignore those legacy names — always use `{YYYY} 想法汇总.md` for new files.

## Summary File Structure (`{YYYY} 想法汇总.md`)

The file is organized by months in reverse chronological order (newest month first). Within each month, entries are also reverse chronological (newest first).

```markdown
# 3月

## 03.17 顶级 AI 的能力被严重低估了

#ai #认知

真正顶级的 AI 搭配顶级的 Agent...（inline content）

## 03.14 通过 App Store 购买了 Claude Max 计划

#ai

今天通过 App Store 购买了...（inline content）

## 03.07 抢泰国 tml，完全抢不到

#活动

早早等待抢泰国 tml 的票...（inline content）

# 2 月

## 02.27 关于 OpenClaw 的想法

#ai

最近在看 OpenClaw...（inline content）

## 02.09 Agent 编程的一些技巧

#ai

来源：https://x.com/...

> [!summary] TL;DR
> ...

### 1) 上下文工程
...（longer structured inline content）
```

### Key formatting details

1. **Month heading**: `# {N}月` — the number is NOT zero-padded. Spacing varies (`# 3月`, `# 2 月`, `# 12 月`), but prefer no space for consistency with the latest entries: `# 3月`.

2. **Entry heading**: `## MM.DD [周X] 标题`
   - MM.DD is zero-padded: `03.17`, `02.09`, `01.05`
   - Weekday (周X) is optional. The 2026 file tends to omit it; the 2025 file includes it for some entries.
   - Title is a concise Chinese description of the thought.

3. **Tags**: On the line immediately after the `##` heading, separated by spaces. Common tags observed:
   - `#ai` — AI and technology related
   - `#认知` — cognition, mindset
   - `#想法` — general ideas
   - `#活动` — events, activities
   - `#方法论` — methodology
   - `#思考` — deep thinking
   - `#记录` — records, logs
   - `#文学` — literature
   - `#规划` — planning
   - Tags end with a trailing space sometimes (e.g., `#ai `) — this is not intentional, just be aware.

4. **Blank line** between tags and content.

5. **Content** is written in the user's natural voice — a mix of casual and reflective Chinese.

## Entry Types

### Type 1: Inline short thought
Everything is in the summary file. No standalone file.
```markdown
## 03.07 抢泰国 tml，完全抢不到

#活动

早早等待抢泰国 tml 的票，结果完全买不带，黄牛票涨的都超过主站了，简直离谱
```

### Type 2: Inline long thought
Structured content with sub-headings, all in the summary file.
```markdown
## 02.09 Agent 编程的一些技巧

#ai

来源：https://x.com/dotey/status/...

> [!summary] TL;DR
> Agent 编程更像...

### 1) 上下文工程
- 把「上下文工程」当成核心...
```

### Type 3: Standalone with embed
Content lives in a separate file, referenced via Obsidian embed in the summary.
```markdown
## 06.05 参加小米股东大会

![[2025-06-05#参加小米股东大会]]
```
The standalone file `2025-06-05.md` starts with:
```markdown
# 参加小米股东大会

正文内容...
```

### Type 4: Standalone with full-file embed (no heading anchor)
```markdown
## 11.24 周一 参加上海 TML 后的一些想法

![[2025-11-24]]
```

## Standalone File Format (`{YYYY-MM-DD}.md`)

- File name: `{YYYY-MM-DD}.md` (e.g., `2025-11-24.md`)
- Starts with `# 标题` as the top-level heading
- Content follows directly
- May contain sub-headings (`##`, `###`) for structure
- Multiple entries in the same day: each gets its own `# 标题` section

## When to Use Standalone vs. Inline

Based on observed patterns:
- **Inline**: Short reflections, quick observations, brief notes (1-2 paragraphs)
- **Standalone**: Long essays, detailed event recaps, structured multi-section thoughts, content with many sub-headings

A rough guideline: if the content would be more than ~300 characters or has internal structure (sub-headings), use a standalone file.

## Obsidian Features Used

- **Callouts**: `> [!tip]`, `> [!summary]`, `> [!note] AI 评价`
- **Embeds**: `![[filename#heading]]`, `![[filename]]`
- **Tags**: Inline `#tag` format (not YAML frontmatter)
- **Images**: `![[image.jpg|300]]` with optional width
- **Links**: Standard markdown links and wikilinks

## AI Evaluation Callout

Each thought entry may include a rational, objective AI evaluation. Always use the `> [!note] AI 评价` callout format, placed after the user's polished content and a blank line, before the next entry's heading:

```markdown
## 08.15 阅读量下降可能不是因为内容变差了

#阅读 #认知 #想法

最近发现自己的阅读量明显下降，一开始以为是推荐算法变差了或者好内容变少了。但仔细想了一下，可能根本原因不在外部——是我的注意力被短视频和社交媒体切得太碎，已经不太习惯长时间专注阅读了。不是内容的问题，是我自己变了。

> [!note] AI 评价
> 这个反思把归因从外部转向了内部，方向是对的。注意力碎片化是一个被广泛讨论但很少被个人认真对号入座的问题。值得进一步追问的是：短视频的"高刺激密度"是否在系统性地拉高了大脑对信息密度的预期，导致文字阅读这种"低刺激密度"的输入方式变得难以忍受。如果这个机制成立，那不只是一个习惯问题，而是一个生理层面的适应性问题。
```

The evaluation should be:
- **Rational and objective**: analyze from a logical, systemic, or structural perspective
- **Not emotional**: avoid empty praise, forced agreement, or subjective cheerleading
- **Substantive**: add analytical depth — connect to broader patterns, surface hidden assumptions, or point out implications the user may not have considered

## Vault Path Resolution

DailyNote files are at `DailyNote/` relative to the vault root. Do NOT hardcode absolute vault paths.

- **obsidian CLI**: all `path=` arguments are vault-relative, so the CLI resolves the absolute path automatically.
- **Fallback**: run `obsidian vault` to discover the vault root, or read `~/Library/Application Support/obsidian/obsidian.json` to find vault directories.

Example using obsidian CLI (vault-relative):
```bash
obsidian read path="DailyNote/{YYYY}/{YYYY} 想法汇总.md"
```
