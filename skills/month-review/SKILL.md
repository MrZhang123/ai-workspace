---
name: month-review
description: Monthly review and next-month planning for Obsidian monthly planning files and quarterly OKR notes. Analyze one month’s progress, map it into each quarterly objective, and update the objective-first monthly review area plus the month overview block without duplicating month headings. Use when the user asks for “月度复盘”“月总结”“下月计划”“OKR 回顾”“OKR 对齐”“month review” or similar month-level review/planning tasks.
---

# Month Review

Use this skill to summarize one month from `Plan/每日规划` and write the result into the matching quarterly OKR note under `Plan/年度规划`.

Read [references/okr-month-review-patterns.md](references/okr-month-review-patterns.md) before editing. It captures the observed 2026 quarterly OKR structure, objective mapping, month-summary layout, and update rules.

## Workflow

1. Resolve the target month. Default to the current month. Honor an explicit month from the user.
2. Locate the monthly planning file and the matching quarterly OKR file. Treat quarter file structure as authoritative and reuse its existing month-review style.
3. Analyze month progress using the counting rules in the reference file. Prefer parent-task counts when parent tasks own child checkboxes. Use nested checkbox progress as supporting detail instead of double-counting.
4. Map the month’s outputs and misses into the quarterly objectives using the reference mapping. Reuse the current quarter's O1-O4 headings exactly as written.
5. Update in place:
   - Append or patch the target month under each objective in the objective-first monthly review area, using the file's local month heading style such as `### 2月`.
   - Append or patch the quarter-level summary block `# 🗓️ YYYY.MM 月度复盘与下月重点`.
   - Do not create duplicate per-objective month headings or duplicate month-summary headings.
6. If the target month is still in progress, say `统计截至 {Today}` in chat output and in the file where needed.
7. Keep insight concise. Prefer one short summary paragraph plus 1-3 next-month actions for each objective over raw task narration.

## Output

- In chat, report work/personal progress, 3-6 milestones, 1-3 key patterns, and next-month focus by objective.
- In file, preserve the local OKR wording and section names already used in the quarterly note.

## Guardrails

- Write to the quarterly OKR file, not to `2026 全年规划.md`.
- Treat the objective-first monthly review area as the primary write target when it exists.
- Support objective headings that are not exact bare `## O1：...` strings, such as emoji-prefixed headings.
- Ignore malformed checklist lines and explanatory bullets without checkboxes.
- If the quarterly OKR file is missing one of the expected objective sections, note the risk and update the existing structure as far as possible without inventing a new OKR taxonomy.
