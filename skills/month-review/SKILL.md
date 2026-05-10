---
name: month-review
description: Monthly review and next-month planning for Obsidian monthly planning files, quarterly OKR notes, and the matching Notion quarterly OKR page. Analyze one month’s progress, map it into each quarterly objective, update both Obsidian and Notion objective-first month review areas, and maintain the next-month focus/candidate pool in the monthly planning file. Use when the user asks for “月度复盘”“月总结”“下月计划”“OKR 回顾”“OKR 对齐”“month review” or similar month-level review/planning tasks.
---

# Month Review

Use this skill to summarize one month from `Plan/每日规划` and write the result into both:

- the matching quarterly OKR note under `Plan/年度规划`
- the matching Notion quarterly OKR page linked from that quarterly note, or found by exact quarter title when no link is present
- the next-month planning file's top-level `{月}重点与候选事项` section, used as the source pool for weekly planning

Read [references/okr-month-review-patterns.md](references/okr-month-review-patterns.md) before editing. It captures the observed 2026 quarterly OKR structure, objective mapping, month-summary layout, Notion mirror layout, and update rules.

## Workflow

1. Resolve the target month. Default to the current month. Honor an explicit month from the user.
2. Locate the files needed:
   - Read the monthly planning file(s) for the target month. Since a month’s tasks may appear across two adjacent month files, read both if the target month contains a week that spans months:
     ```bash
     obsidian read path="Plan/每日规划/{YYYY}/Q{Q}/{YYYY.MM}.md"
     ```
   - Locate and read the matching quarterly OKR file. Map the target month to its quarter first: months 1-3 → `第一季度`, 4-6 → `第二季度`, 7-9 → `第三季度`, 10-12 → `第四季度`. Use `obsidian search query="{YYYY} 第"` if the exact filename is uncertain, then read it:
     ```bash
     obsidian read path="Plan/年度规划/{YYYY} OKR/{YYYY} 第{一|二|三|四}季度.md"
     ```
   - Locate the matching Notion quarterly OKR page. Prefer an explicit Notion URL in the quarterly note; otherwise search Notion by the exact title, such as `2026 第二季度`.
   Treat the quarter file structure as authoritative and reuse its existing month-review style in both destinations.
3. Analyze month progress using the counting rules in the reference file. Prefer parent-task counts when parent tasks own child checkboxes. Use nested checkbox progress as supporting detail instead of double-counting.
4. Map the month’s outputs and misses into the quarterly objectives using the reference mapping. Reuse the current quarter’s O1-O4 headings exactly as written.
5. For each objective, include a short `稳定推进情况与原因判断` subsection by default:
   - name what moved steadily and why
   - name what repeatedly slipped or stalled
   - judge the dominant causes, such as changing requirements, parallel work, missing prerequisites, unclear ownership, lack of protected time, work compressing personal time, unstable sleep, low energy, weak morning routine, or poor evening focus
   - turn the cause judgment into concrete next-month adjustments
6. Update in place in the quarterly OKR file:
   - If appending a new month section under an objective, use `obsidian append path="..." content="..." silent`.
   - If patching an existing month placeholder or summary block, use the Edit tool directly on the vault file.
   - Do not create duplicate per-objective month headings or duplicate month-summary headings.
7. Update the matching Notion quarterly OKR page with the same month-review content:
   - Fetch the Notion page before editing and inspect the existing `# 📋 分项回顾` area.
   - Use the Notion update tool to patch only the relevant section. Preserve inline databases, child pages, callouts, tables, and unrelated content.
   - If the month section already exists in Notion, replace that month’s block instead of appending another `### {M}月`.
   - If the Notion page cannot be found after checking the note link and exact-title search, report that blocker clearly and do not present the task as fully finished.
8. Update the next-month planning file's `{月}重点与候选事项` section:
   - Use the section as a month-level priority pool, not as a week plan.
   - Place it after the file header embeds and before the newest week block.
   - If a similar section already exists, merge and update it instead of creating a duplicate.
   - Preserve completed status from existing week plans, and keep all carry-over or candidate items unless they are clearly obsolete.
   - Use the structure `本月主线` / `P0：必须推进` / `P1：应该推进，但不都压到同一周` / `P2：候选事项`.
9. For quarter-end months (3月/6月/9月/12月), also generate the `# 🏖️ 整体评价` section (达成度 table, core outputs, highlights, problems with `[!warning]` callout, next-quarter focus with `[!tip]` callout) and place it before the `# 📋 分项回顾` section in both Obsidian and Notion. See the reference file for the exact template and callout usage.
10. If the target month is still in progress, say `统计截至 {Today}` in chat output and in both written destinations where needed.
11. Keep insight concise. Prefer one short summary paragraph plus 1-3 next-month actions for each objective over raw task narration.
12. In chat output, always add two explicit sections after the month summary:
   - `特别注意的事情`: call out carry-over items, blocked objectives, slipping KRs, structural problems, and any planning-vs-execution mismatch that the user should notice quickly.
   - `接下来特别需要推进的事项`: group next actions into `P0 / P1 / 可延后`, prioritizing items that unblock the next month or reduce accumulation risk.
13. Treat month review as a **medium-length summary**, not as a weekly-style quick note:
   - It should usually be more detailed than `weekly-review`, because the user needs to see objective-level momentum, not just this week's issues.
   - Keep the structure fixed and scannable; avoid drifting into a long chronological replay.
   - For non-quarter-end months, a good default is:
     - `OKR / 月度进展总览`
     - `整体评价`
     - `关键观察`
     - `稳定推进情况与原因判断`
     - `特别注意的事情`
     - `接下来特别需要推进的事项`
   - For quarter-end months, keep the fuller quarter-end structure from the reference file.

## Output

- In chat, report work/personal progress, 3-6 milestones, 1-3 key patterns, and next-month focus by objective.
- Recommended chat structure:
  - `OKR / 月度进展总览`
  - `整体评价`
  - `关键观察`
  - `稳定推进情况与原因判断`
  - `特别注意的事情`
  - `接下来特别需要推进的事项`
  - If the month is still in progress, prepend `统计截至 {Today}`.
- In written destinations, preserve the local OKR wording and section names already used in the quarterly note, Notion page, and monthly planning file.

## Guardrails

- If Obsidian is not running, fall back to reading vault files directly with the Read tool.
- Write to the quarterly OKR file, the matching Notion quarterly OKR page, and the next-month planning file's focus/candidate section; do not write to `2026 全年规划.md`.
- Treat the objective-first monthly review area as the primary write target when it exists.
- Fetch the Notion page before editing it. Never replace the whole page unless the user explicitly asks and child databases/pages are preserved.
- Do not delete monthly candidate items merely because they were not selected for the next week; move them to P1/P2 if they still matter.
- Support objective headings that are not exact bare `## O1：...` strings, such as emoji-prefixed headings.
- Ignore malformed checklist lines and explanatory bullets without checkboxes.
- If the quarterly OKR file is missing one of the expected objective sections, note the risk and update the existing structure as far as possible without inventing a new OKR taxonomy.
