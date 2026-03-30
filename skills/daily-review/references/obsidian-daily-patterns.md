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

### Variant C: Minimal plan, no review

Observed for weekends and days with only personal tasks. Flatter heading structure, no `### 今日规划` or `#### 今天的 Top Goal` wrappers, no review section.

```markdown
## 03.21 周六

> 一句话引言

### 个人
- [ ] P0: ...
- [ ] P1: ...

### 备注
- ...
```

Key differences from Variant A/B:
- Quote block directly after the day heading (no `### 今日规划`)
- Sections use `###` (h3) directly: `### 工作`, `### 个人`, `### 备注`
- No `#### 今天的 Top Goal 是什么？` wrapper
- No review section — used when the user explicitly says no review is needed, or for weekend/light days

**Only use Variant C on weekends (Saturday/Sunday).** Weekdays (Monday–Friday) must use Variant A or B with full plan structure and review section.

### Review Section Names

The notes contain these names across different periods:

- `### 昨日回顾` (early 2026)
- `### 今日全天回顾` (January–March 2026, legacy format)
- `### 今日回顾` (April 2026 onward, current format)

**From April 2026 onward, use `### 今日回顾` with the compact review format (see Variant D below).**

For files before April 2026, preserve the existing review section name when editing.

### Variant D: Compact review (April 2026 onward)

Replaces the old multi-heading review format. Designed for 30-second completion at night.

```markdown
### 今日回顾

- 达成：工作 ○○○ | 个人 ○○○○
- 卡点（1 句话）：
- 精力（上午/下午/晚上）：
- 作息：
- 健身：
- 明早第一件事：
```

Filled example:

```markdown
### 今日回顾

- 达成：工作 ●●○ | 个人 ●○○○
- 卡点（1 句话）：下班后太累，英语没启动
- 精力（上午/下午/晚上）：好/一般/差
- 作息：22:30 睡 / 7:00 起
- 健身：有氧 30min
- 明早第一件事：7:00 起，读 30min 致股东信
```

Field guide:
- **达成**: one ● or ○ per parent task in the plan section. ● = done, ○ = not done. Separated into 工作 and 个人. Count the plan's parent-level checkboxes to determine how many circles to generate.
- **卡点**: one sentence describing the main blocker, or `无` if smooth. Feeds into weekly review diagnostics.
- **精力**: three slots, each `好`/`一般`/`差`. Accumulates into weekly energy pattern analysis.
- **作息**: actual sleep and wake times. Core tracking data for the Q2 schedule adjustment goal.
- **健身**: free-form (e.g., `有氧 30min` or `否`)
- **明早第一件事**: tomorrow's first personal action, decided tonight to reduce morning activation cost. This is the most important field.

Field guide:
- **工作/个人**: completed/total parent task counts (e.g., `2/3`)
- **卡点**: one sentence describing the main blocker, or `无` if smooth. Feeds into weekly review diagnostics.
- **精力**: three slots, each `好`/`一般`/`差`. Accumulates into weekly energy pattern analysis.
- **作息**: actual sleep and wake times. Core tracking data for the Q2 schedule adjustment goal.
- **健身**: free-form (e.g., `有氧 30min` or `否`)
- **明早第一件事**: tomorrow's first personal action, decided tonight to reduce morning activation cost. This is the most important field.

## 3. Update Rules

- If the target day heading exists but has no body, complete that block instead of inserting a second heading.
- If the day block already contains a review section, keep its title and subsection names.
- If the week's recent days use the compact layout, keep using it for consistency.
- If no local precedent exists, fall back to Variant A.

### Day Block Ordering (CRITICAL)

Day blocks within a week are ordered **newest first** (descending). The most recent date always appears immediately after the week-level overview (`## 工作` / `## 个人` sections), with older dates below.

```
# 03.16～03.22 第三周
## 工作
...
## 个人
...

## 03.18 周三   ← newest, immediately after the week overview
## 03.17 周二
## 03.16 周一   ← oldest at the bottom
```

When inserting a new day block, **always place it directly after the week overview, before any existing day headings**. Never append it after older day blocks.

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
- Keep subjective fields blank unless the note already contains objective facts written by the user.
- For the compact review (Variant D), pre-fill `工作` and `个人` counts if completion data is available. Leave all other fields blank for the user to fill.
- Never pre-fill `卡点`, `精力`, `作息`, or `明早第一件事` — these are subjective and must come from the user.
