---
name: weekly-review
description: Weekly review and next-week planning for Obsidian monthly planning files. Analyze the current or specified week, read the month-level focus/candidate pool, infer the local section style, summarize milestones and risks, and update one week-level review section inside the week block without nesting it under personal subheadings. Use when the user asks for “周复盘”“本周总结”“下周计划”“这周进度怎么样”“weekly review”“week summary” or similar week-level review/planning tasks.
---

# Weekly Review

Use this skill to update one week block inside `Plan/每日规划/{YYYY}/Q{Q}/{YYYY.MM}.md`.

Read [references/obsidian-weekly-patterns.md](references/obsidian-weekly-patterns.md) before editing. It captures the observed 2026 week structures, naming variants, insertion boundaries, counting rules, and fallback template.

## Workflow

### Phase 1: 收集信息

1. Resolve the target week. Default to the current week. Honor an explicit date range or week name from the user.
2. **Read the quarterly OKR** to understand the season's goals and priorities:
   - Obsidian: `Plan/年度规划/2026 OKR/{YYYY} 第{N}季度.md` (e.g. `2026 第二季度.md`)
   - Notion: search for the same name (e.g. `2026 第二季度`), fetch the page, and read the Overview / KeyResult / ToDo databases to get status and completion data.
   - Obsidian and Notion use the same naming convention for quarterly OKR, so search Notion by the same title.
3. Find candidate month files. Read the current month file first:
   ```bash
   obsidian read path="Plan/每日规划/{YYYY}/Q{Q}/{YYYY.MM}.md"
   ```
   Also inspect the adjacent month file when the week spans two months. If the exact path is uncertain, use `obsidian search query="{week heading text}"` to locate the right file. Treat the week heading text as the source of truth even when the span is not a standard 7-day week.
4. Read the top-level `{月}重点与候选事项` section when present. Treat it as the month-level priority pool for next-week planning:
   - P0 items are the first source for next-week tasks.
   - P1 items should be selected only when the week has enough capacity.
   - P2 items stay as candidates unless the user explicitly promotes them or the week has clear spare capacity.

### Phase 2: 分析与输出进度（先在 chat 中展示，不写文件）

5. **Output a quarterly OKR progress overview in chat.** For each Objective:
   - List every KR and its current status (未启动 / 进行中 / 已完成).
   - Highlight this week's relevant progress against each KR.
   - Default to a flat bullet-list format grouped by Objective. Avoid tables unless the user explicitly asks for them.
6. **Analyze remaining time and output priority recommendations in chat:**
   - How many workdays / weekend days remain in the week.
   - Account for fixed constraints such as leave days, travel, appointments, shareholder meetings, health treatment, or document/account errands before estimating capacity.
   - Add a dedicated `特别注意的事情` section:
     - Include carry-over items, blocking dependencies, KRs falling behind pace, and any mismatch between week-level planning and daily records that could distort completion judgment.
     - Keep it factual and concise so the user can immediately see what needs attention.
   - Add a dedicated `接下来特别需要推进的事项` section:
     - Use `P0 / P1 / 可延后` to show what must move this week, what should move if time allows, and what is safe to defer.
     - Prioritize items that unblock Objectives, reduce carry-over risk, or need protected deep-work time.
   - **P0 (must do)**: items that are time-sensitive, blocking, or directly aligned with high-priority KRs.
   - **P1 (should push)**: items that advance KRs but are not urgent this week.
   - **Can defer**: items safe to push to next week with rationale.
   - Preserve the source priority labels. Do not describe a P1 task as P0 unless the user explicitly promotes it or the current week plan already does so.
   - Call out risks: carry-over items, KRs falling behind pace, blockers.
   - Keep next-week plans concise: prefer parent tasks and clear priorities; add subtasks only for concrete deliverables, deadlines, or known constraints. Default to 1-2 main P0 focuses for the week; move other items into light parallel work or deferral.
7. If the week is still in progress, say `统计截至 {Today}` in chat output.
8. **Wait for user confirmation before writing to the file.** The user may want to adjust priorities or add/remove items.

### Phase 3: 写入文件

9. Detect the local weekly style from the current file. Reuse the existing section name if the file already uses `周总结`, `本周总结`, or `📝 本周复盘`.
10. Update in place:
   - If a weekly review section already exists in the target week block, update that section instead of creating a second one.
   - Insert the weekly review at week-block top level, after the weekly goal sections and before the first day heading.
   - Match the heading depth used by sibling week-level sections and day headings. Do not nest the review under `## 个人` or any category subsection.
   - For inserting a new review section, use `obsidian append path="..." content="..." silent`. For patching an existing section, use the Edit tool directly on the vault file.
11. Analyze progress using the counting rules in the reference file. Prefer parent-task counts when parent tasks own child checkboxes.
12. Produce a concise summary with milestones, risks, and next-step priorities. Prefer insight over task-by-task narration.
13. For the file version, default to a compact structure unless the local note clearly uses a longer established style:
   - `评分与进度`
   - `一句话总结`
   - `核心产出`
   - `关键观察`
   - `顺延项判断`
   - `下周安排`
   - `特别注意`
   Collapse repetitive sections such as `节奏与状态` / `主要问题（事实层）` / `下周调整（可执行）` into the bullets above unless they add distinct signal.
14. In `评分与进度`, include a numeric 1-10 score and brief anchors when evidence supports it: work-side score, personal-side score, and whether the trend is up/down/flat versus the prior week.
15. In `核心产出`, split real deliverables from input or learning. Use labels like `已形成输出` and `已完成输入` when the week has both.
16. In `顺延项判断`, classify recurring carry-over items one by one. State whether to keep the current priority, suggest downgrading, move to a better time slot, or defer. Priority changes should be phrased as recommendations unless the user has decided them.

## Output

- **In chat (Phase 2)**: quarterly OKR progress overview per Objective, this week's progress mapping, remaining time analysis, priority-ranked task recommendations (P0/P1/defer), risks and blockers.
- **Recommended chat structure (Phase 2)**:
  - `OKR 进展总览`
  - `评分与进度`
  - `特别注意`
  - `下周安排`
  - If the week is still in progress, prepend `统计截至 {Today}`.
- **Recommended file structure (Phase 3)**:
  - `评分与进度`
  - `一句话总结`
  - `核心产出`
  - `关键观察`
  - `顺延项判断`
  - `下周安排`
  - `特别注意`
- **In file (Phase 3)**: preserve the local naming and tone instead of forcing a new review title. Write the weekly review section only after user confirmation.

## Guardrails

- If Obsidian is not running, fall back to reading vault files directly with the Read tool.
- Support non-standard week spans such as holiday blocks. Do not assume every week covers exactly seven days.
- When planning a new week, use the month-level focus/candidate section as the priority source and preserve the P0/P1/P2 intent unless the user changes it.
- Keep week plans easy to execute. Avoid breaking every task into procedural microsteps; use short notes instead when a constraint or timing preference matters.
- Keep the edit inside the target week block and before the next week heading.
- Ignore malformed checklist lines and explanatory bullets without checkboxes.
- If more than one week heading could match, prefer the heading explicitly named by the user or the one containing today's date. If ambiguity remains, explain it before editing.
- **Never write to the file before showing the progress analysis in chat and getting user confirmation.**
