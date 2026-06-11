---
name: daily-review
description: Daily review and day-level planning for Obsidian monthly planning files. Analyze one day’s completion, read the user’s Feishu/Lark calendar before drafting today/tomorrow plans, infer the local note style, write a concise fact-based review with completed work, unfinished work, cause judgment, tomorrow adjustment, and update the target day block without creating duplicate headings. Use when the user asks for “每日复盘”“今天总结”“今日规划”“明日规划”“补今日回顾”“补明天计划”“今天完成了什么”“明天做什么”“daily review” or similar day-level review/planning tasks.
---

# Daily Review

Use this skill to update one day block inside `Plan/每日规划/{YYYY}/Q{Q}/{YYYY.MM}.md`.

Read [references/obsidian-daily-patterns.md](references/obsidian-daily-patterns.md) before editing. It captures the observed 2026 file structure, naming variants, counting rules, and fallback templates.

## Workflow

1. Resolve the target day. Default to reviewing today and planning tomorrow. Honor explicit dates from the user.
2. For any day-level planning request, read the user's Feishu/Lark calendar before drafting tasks:
   ```bash
   lark-cli calendar +agenda --start YYYY-MM-DD --end YYYY-MM-DD --format json
   ```
   - Use the target date for both `--start` and `--end`; for "today", also check the current local time before allocating remaining time.
   - Treat accepted busy events as fixed time blocks. Avoid scheduling deep work during those blocks.
   - If events overlap, prioritize accepted work/meeting events over optional or `needs_action` events, and mention important conflicts in chat.
   - If calendar auth is missing or the command fails, follow the `lark-calendar` auth flow when the user can authorize; otherwise state that calendar data was unavailable and continue from the Obsidian plan.
3. Find candidate month files for the target day and its week. Read the target month file with:
   ```bash
   obsidian read path="Plan/每日规划/{YYYY}/Q{Q}/{YYYY.MM}.md"
   ```
   Inspect adjacent months when the week crosses month boundaries. If the exact path is uncertain, use `obsidian search query="{MM.DD}"` to locate the right file. Prefer the file that already contains the target week heading or target day heading.
4. Detect the local style from the nearest completed day blocks in the same week. Reuse heading depth, section names, and block layout before falling back to a default template.
5. Update in place:
   - If the target day heading already exists, fill only missing sections or obviously empty placeholders.
   - If the target day heading exists but is empty, complete that block instead of creating a new heading.
   - If the day block already contains a review section, preserve the existing name and structure.
   - **Day block order is newest-first**: when inserting a new day block, place it directly after the week-level overview sections (`## 工作` / `## 个人`), before any existing day headings. Never append after older blocks.
   - For patching existing sections, use the Edit tool directly on the vault file.
6. Analyze progress using the counting rules in the reference file. Prefer parent-task counts when a task owns child checkboxes. Use child completion as supporting detail instead of double-counting.
7. After drafting the day's review, reconcile completed daily tasks against the current week's top-level checklist. If a checked daily parent task clearly completes the same weekly parent task, update the weekly checkbox from `[ ]` to `[x]`. Use the "Weekly checkbox sync" rules in the reference file; when the match is uncertain or only partial, leave the weekly checkbox unchanged and mention the possible mismatch in chat.
8. Write today/tomorrow plans against real calendar capacity: carry over unfinished P0 items first, keep fixed meetings visible in the plan when they drive task choices, then add at most 1-2 new tasks that fit the open time blocks. On meeting-heavy days, prefer small preparation, notes, and follow-up tasks over large deep-work items.
   - Do not turn the plan into a clock-based timetable by default. Use priority/task checklist bullets. Include exact times only for existing calendar events, actual sleep/wake records, or when the user explicitly asks for time-boxing.
9. Review field drafting policy (Variant D, April 2026 onward): draft fields that can be justified from objective sources in the file; leave subjective fields blank. See the "Review field policy" table in the reference file for exact rules.
   - **AI drafts**: `达成` counts (mechanical), `今日完成`, `未完成`, `明日调整`, and cautious `原因判断` only when the cause is visible in the plan section or notes.
   - **User writes**: `精力（上午/下午/晚上）`, `作息`, `健身`, and any `原因判断` whose real cause is internal (mood, distraction, unrecorded context).
   - **Empty beats fabricated**: for subjective fields, leaving blank is always preferable to guessing. These fields feed the user's Q2 energy-strategy data loop — fabricated values corrupt that data permanently. If unsure, leave blank.
   - When drafting `原因判断`, clearly base it on file-visible facts (incomplete tasks + priorities + carry-over history + explicit notes). If the likely cause is emotional/internal, leave blank rather than guess.
10. For files from April 2026 onward, use the concise review format (Variant D in the reference file). For files before April 2026, preserve the existing review format.

## Output

- In chat, report done/todo counts, the most important carry-over risk, and 2-3 concrete suggestions.
- For planning updates, briefly mention the calendar constraints used, especially dense meeting blocks or conflicts that changed the task plan. Keep this as a short capacity note, not a list of task time ranges.
- In chat, report any weekly checklist items that were synced, and any likely weekly/daily mismatch left unchanged because the match was not certain.
- In file, for April 2026 onward use `### 今日回顾` with the concise format (Variant D). For older files, preserve the existing section names such as `今日全天回顾` or `昨日回顾`.

## Guardrails

- If Obsidian is not running, fall back to reading vault files directly with the Read tool.
- Treat day-level requests only. A pure “本周进度怎么样” request belongs to `weekly-review` unless the user also asks for tomorrow planning.
- Keep the edit inside the current week block.
- Ignore malformed checklist lines and explanatory bullets without checkboxes.
- If more than one candidate week block matches, choose the one whose heading text explicitly contains the target date. If ambiguity remains, explain it before editing.
