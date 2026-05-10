---
name: daily-review
description: Daily review and tomorrow planning for Obsidian monthly planning files. Analyze one day’s completion, infer the local note style, write a concise fact-based review with completed work, unfinished work, cause judgment, tomorrow adjustment, and update the target day block without creating duplicate headings. Use when the user asks for “每日复盘”“今天总结”“明日规划”“补今日回顾”“补明天计划”“今天完成了什么”“明天做什么”“daily review” or similar day-level review/planning tasks.
---

# Daily Review

Use this skill to update one day block inside `Plan/每日规划/{YYYY}/Q{Q}/{YYYY.MM}.md`.

Read [references/obsidian-daily-patterns.md](references/obsidian-daily-patterns.md) before editing. It captures the observed 2026 file structure, naming variants, counting rules, and fallback templates.

## Workflow

1. Resolve the target day. Default to reviewing today and planning tomorrow. Honor explicit dates from the user.
2. Find candidate month files for the target day and its week. Read the target month file with:
   ```bash
   obsidian read path="Plan/每日规划/{YYYY}/Q{Q}/{YYYY.MM}.md"
   ```
   Inspect adjacent months when the week crosses month boundaries. If the exact path is uncertain, use `obsidian search query="{MM.DD}"` to locate the right file. Prefer the file that already contains the target week heading or target day heading.
3. Detect the local style from the nearest completed day blocks in the same week. Reuse heading depth, section names, and block layout before falling back to a default template.
4. Update in place:
   - If the target day heading already exists, fill only missing sections or obviously empty placeholders.
   - If the target day heading exists but is empty, complete that block instead of creating a new heading.
   - If the day block already contains a review section, preserve the existing name and structure.
   - **Day block order is newest-first**: when inserting a new day block, place it directly after the week-level overview sections (`## 工作` / `## 个人`), before any existing day headings. Never append after older blocks.
   - For patching existing sections, use the Edit tool directly on the vault file.
6. Analyze progress using the counting rules in the reference file. Prefer parent-task counts when a task owns child checkboxes. Use child completion as supporting detail instead of double-counting.
7. Write tomorrow's plan with carry-over P0 items first, then add at most 1-2 new tasks that align with the current week.
8. Review field drafting policy (Variant D, April 2026 onward): draft fields that can be justified from objective sources in the file; leave subjective fields blank. See the "Review field policy" table in the reference file for exact rules.
   - **AI drafts**: `达成` counts (mechanical), `今日完成`, `未完成`, `明日调整`, and cautious `原因判断` only when the cause is visible in the plan section or notes.
   - **User writes**: `精力（上午/下午/晚上）`, `作息`, `健身`, and any `原因判断` whose real cause is internal (mood, distraction, unrecorded context).
   - **Empty beats fabricated**: for subjective fields, leaving blank is always preferable to guessing. These fields feed the user's Q2 energy-strategy data loop — fabricated values corrupt that data permanently. If unsure, leave blank.
   - When drafting `原因判断`, clearly base it on file-visible facts (incomplete tasks + priorities + carry-over history + explicit notes). If the likely cause is emotional/internal, leave blank rather than guess.
9. For files from April 2026 onward, use the concise review format (Variant D in the reference file). For files before April 2026, preserve the existing review format.

## Output

- In chat, report done/todo counts, the most important carry-over risk, and 2-3 concrete suggestions.
- In file, for April 2026 onward use `### 今日回顾` with the concise format (Variant D). For older files, preserve the existing section names such as `今日全天回顾` or `昨日回顾`.

## Guardrails

- If Obsidian is not running, fall back to reading vault files directly with the Read tool.
- Treat day-level requests only. A pure “本周进度怎么样” request belongs to `weekly-review` unless the user also asks for tomorrow planning.
- Keep the edit inside the current week block.
- Ignore malformed checklist lines and explanatory bullets without checkboxes.
- If more than one candidate week block matches, choose the one whose heading text explicitly contains the target date. If ambiguity remains, explain it before editing.
