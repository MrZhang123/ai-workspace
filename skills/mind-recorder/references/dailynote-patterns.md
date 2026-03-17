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

- **Callouts**: `> [!tip]`, `> [!summary]`
- **Embeds**: `![[filename#heading]]`, `![[filename]]`
- **Tags**: Inline `#tag` format (not YAML frontmatter)
- **Images**: `![[image.jpg|300]]` with optional width
- **Links**: Standard markdown links and wikilinks

## Vault Path Resolution

DailyNote files are at `DailyNote/` relative to the vault root. Do NOT hardcode absolute vault paths.

- **obsidian CLI**: all `path=` arguments are vault-relative, so the CLI resolves the absolute path automatically.
- **Fallback**: run `obsidian vault` to discover the vault root, or read `~/Library/Application Support/obsidian/obsidian.json` to find vault directories.

Example using obsidian CLI (vault-relative):
```bash
obsidian read path="DailyNote/{YYYY}/{YYYY} 想法汇总.md"
```
