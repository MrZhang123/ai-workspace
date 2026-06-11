# Obsidian Weekly Patterns

Use this reference when updating one week block in the monthly planning notes under `Plan/每日规划`.

## 1. File Resolution

- Search the target month file first, then inspect adjacent months when the week spans two months.
- Trust the week heading text as the source of truth. The note may contain spans such as `01.26～02.01`, `02.25～03.01`, or holiday ranges like `02.14～02.24 第三周（春节放假）`.
- If the current week already exists in a prior month's file, update that file instead of creating a duplicate week block in the new month.

## 2. Week Block Ordering (Reverse Chronological)

Month files list week blocks in **reverse chronological order**. If the file has a top-level `{月}重点与候选事项` section, the newest week appears immediately after that section. When inserting a new week block, place it after the month-level focus/candidate section and before the most recent existing week heading, not after the last daily entry.

Example layout:
```
![[规划记录#原则]]
# 个人 OKR
![[2026 第二季度]]
# 2026 ToDo 池
![[2026 ToDo 池]]

# 五月重点与候选事项
...

# 04.08～04.12 第二周    ← newest week (insert here)
...
# 03.30～04.05 第一周    ← older week
...
```

Verified in `2026.03.md`: 第四周 (line 12) → 第三周 (line 279) → 第二周 (line 508) → 第一周 (line 724).

## 3. Observed Weekly Review Variants

The 2026 notes already use multiple section names and depths.

### Existing review titles

- `## 周总结`
- `## 本周总结`
- `## 📝 本周复盘 (Weekly Review)`
- `### 📝 本周复盘（Weekly Review）`

The `###` variant is structurally risky because it can end up nested under `## 个人`. Prefer the file's existing review title when one already exists. If no weekly review section exists yet, use a top-level week section such as `## 本周总结`.

## 4. Insertion Boundary

Insert or update the weekly review:

- inside the target week block
- after the weekly goal sections such as `## 工作`, `## 个人`, and their subcategories
- before the first day heading such as `## 03.02 周一`

This keeps the review as a sibling of the week-level sections instead of accidentally nesting it under a category section.

## 4.1 Month-Level Focus/Candidate Section

When planning a new week, read the top-level `{月}重点与候选事项` section first if present:

- `本月主线` explains the month's work/personal direction and scheduling constraints.
- `P0` items should drive the next week plan.
- `P1` items are selected based on capacity.
- `P2` items usually remain candidates.

Do not copy the whole monthly pool into one week. Select a realistic subset, preserve existing completed status, and call out items that remain unplanned.

## 5. Counting Rules

- Count parent tasks as the primary unit for headline completion metrics.
- If a parent task contains child checkboxes, use the parent task in the top-line completion rate and mention child progress only as supporting detail.
- Separate work and personal metrics.
- Keep `P0`, `P1`, and untagged tasks separate when the data supports it.
- Ignore malformed checklist lines and explanatory bullets without checkboxes.

## 6. Preferred Content

Prioritize:

- A scored progress assessment with brief anchors. When evidence supports it, include work-side score, personal-side score, and trend versus the prior week.
- 1-3 milestone-style outputs, not a raw task dump. Split real deliverables from input or learning when both exist.
- 1-2 factual bottlenecks
- Specific carry-over judgment: classify repeated unfinished items one by one instead of saying only "continue next week".
- a compact review structure that is quick to scan on revisit
- 2-3 next-step priorities with clear triggers or minimal closure. Prefer 1-2 main P0 focuses and put the rest into light parallel work or deferral.
- concise week plans with parent tasks; avoid nested step lists unless the detail is a real deadline, deliverable, or constraint

Priority and evidence rules:

- Preserve source priority labels. Do not turn a P1 item into P0 unless the user explicitly promoted it or the week plan already says so.
- Suggested downgrades should be written as recommendations, not as completed decisions.
- Call out day-record gaps or week-after completion marks when they affect evidence quality.
- Account for fixed constraints such as leave, travel, appointments, shareholder meetings, health treatment, passport pickup, or account setup before estimating capacity.

If no local weekly review style exists yet, use this fallback:

```markdown
## 本周总结

### 评分与进度
- 评分（1-10）：
	- 工作侧：
	- 个人侧：
	- 综合判断：
- 父任务完成情况：

### 一句话总结
- 待填写

### 核心产出
- 已形成输出：
- 已完成输入：

### 关键观察
- 待填写

### 顺延项判断
- 待填写

### 下周安排
- 本周主攻：
- 必须处理的固定事项：
- 轻量并行：
- 明确延后：

### 特别注意
- 待填写
```
