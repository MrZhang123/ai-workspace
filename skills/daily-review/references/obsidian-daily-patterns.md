# Obsidian Daily Patterns

Use this reference when updating a day block in the monthly planning notes under `Plan/每日规划`.

## 1. File Resolution

- Trust the week heading in the note, not the calendar month alone.
- Search the target month file first, then the adjacent month when the week crosses months.
- A week may span two months, for example `01.26～02.01` in `2026.01.md` and `02.25～03.01` in `2026.02.md`.
- If the target day heading already exists in one file, edit that file even if the calendar date belongs to the next month.

## 2. Observed Day Block Variants

The 2026 notes already use multiple day-block styles. Reuse the nearest local style instead of forcing one template.

### Variant A: Full plan + full review

Common in late January and much of February.

```markdown
## 02.10 周二

### 今日规划

#### 今天的 Top Goal 是什么？

##### 工作
- [ ] ...

##### 个人
- [ ] ...

#### 今天不做什么？为什么？

### 今日全天回顾

#### 今日全天的效率如何？（评分 1-10）
- 效率评分（1–10）：
- 深度工作时长（分钟）：
- 目标达成（工作/个人）：
```

### Variant B: Compact plan + notes

Observed in March.

```markdown
## 03.03 周二

### 今日规划

#### 工作
- [ ] ...

#### 个人
- [ ] ...

#### 备注

### 今日全天回顾
```

### Review Section Names

The notes already contain all of these names:

- `### 昨日回顾`
- `### 今日回顾`
- `### 今日全天回顾`

Prefer the dominant naming used in the same file and nearby days.

## 3. Update Rules

- If the target day heading exists but has no body, complete that block instead of inserting a second heading.
- If the day block already contains a review section, keep its title and subsection names.
- If the week's recent days use the compact layout, keep using it for consistency.
- If no local precedent exists, fall back to Variant A.

## 4. Counting Rules

- Count parent tasks as the primary unit for completion metrics.
- If a parent task contains child checkboxes, do not count both the parent and every child in the headline completion rate.
- Use child completion only to explain progress within a parent task.
- Ignore malformed checklist lines such as unfinished `- [ ] P`.
- Ignore explanatory bullets without checkboxes.
- Use `P0` and `P1` when present; otherwise label as untagged.

## 5. What to Write

- Write tomorrow planning tasks and blank review placeholders.
- Carry over unfinished `P0` items first.
- Limit new tasks. Prefer 1-2 new tasks with clear closure over a long list.
- Keep subjective fields blank unless the user already wrote objective facts that can be safely preserved.
