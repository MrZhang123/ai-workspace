# Obsidian Weekly Patterns

Use this reference when updating one week block in the monthly planning notes under `Plan/每日规划`.

## 1. File Resolution

- Search the target month file first, then inspect adjacent months when the week spans two months.
- Trust the week heading text as the source of truth. The note may contain spans such as `01.26～02.01`, `02.25～03.01`, or holiday ranges like `02.14～02.24 第三周（春节放假）`.
- If the current week already exists in a prior month's file, update that file instead of creating a duplicate week block in the new month.

## 2. Observed Weekly Review Variants

The 2026 notes already use multiple section names and depths.

### Existing review titles

- `## 周总结`
- `## 本周总结`
- `## 📝 本周复盘 (Weekly Review)`
- `### 📝 本周复盘（Weekly Review）`

The `###` variant is structurally risky because it can end up nested under `## 个人`. Prefer the file's existing review title when one already exists. If no weekly review section exists yet, use a top-level week section such as `## 本周总结`.

## 3. Insertion Boundary

Insert or update the weekly review:

- inside the target week block
- after the weekly goal sections such as `## 工作`, `## 个人`, and their subcategories
- before the first day heading such as `## 03.02 周一`

This keeps the review as a sibling of the week-level sections instead of accidentally nesting it under a category section.

## 4. Counting Rules

- Count parent tasks as the primary unit for headline completion metrics.
- If a parent task contains child checkboxes, use the parent task in the top-line completion rate and mention child progress only as supporting detail.
- Separate work and personal metrics.
- Keep `P0`, `P1`, and untagged tasks separate when the data supports it.
- Ignore malformed checklist lines and explanatory bullets without checkboxes.

## 5. Preferred Content

Prioritize:

- 1-3 milestone-style outputs, not a raw task dump
- 1-2 factual bottlenecks
- 2-3 next-week adjustments with clear triggers or minimal closure

If no local weekly review style exists yet, use this fallback:

```markdown
## 本周总结

### 进度评估
- 评分（1-10）：
- 核心产出：
- 完成率（按周块任务统计）：

### 一句话总结
- 

### 节奏与状态
- 

### 关键观察
- 

### 主要问题（事实层）
- 

### 下周调整（可执行）
- 
```
