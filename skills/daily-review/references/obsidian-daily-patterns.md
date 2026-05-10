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

**From April 2026 onward, use `### 今日回顾` with the concise review format (see Variant D below).**

For files before April 2026, preserve the existing review section name when editing.

### Variant D: Concise review (April 2026 onward)

Replaces the old multi-heading review format. Designed for a 1-2 minute review that remains easy to fill but still contains enough detail for weekly and monthly review.

```markdown
### 今日回顾

- 达成：工作 ○○○ | 个人 ○○○○
- 今日完成：
- 未完成：
- 原因判断：
- 明日调整：
- 精力（上午/下午/晚上）：
- 作息：
- 健身：
- 明早第一件事：
```

Filled example:

```markdown
### 今日回顾

- 达成：工作 ●●○ | 个人 ●○○○
- 今日完成：完成荣誉体系页面主流程和分享材料大纲。
- 未完成：荣誉体系联调和财务数据方案仍未推进。
- 原因判断：下午会议占用较多时间，个人项安排偏多。
- 明日调整：上午先处理荣誉体系联调；个人侧只保留财务数据方案的 30min 对比记录。
- 精力（上午/下午/晚上）：好/一般/差
- 作息：23:30 睡 / 7:00 起
- 健身：有氧 30min
- 明早第一件事：7:00 起，读 30min 致股东信
```

Field guide:
- **达成**: one ● or ○ per parent task in the plan section. ● = done, ○ = not done. Separated into 工作 and 个人. Count the plan's parent-level checkboxes to determine how many circles to generate. Partly completed parent tasks still count as ○; mention real progress in `今日完成`.
- **今日完成**: factual outputs and visible progress from checked parent tasks, checked child tasks, or explicit notes. Keep it concrete and avoid overclaiming.
- **未完成**: unfinished parent tasks and important unfinished child tasks, especially P0 items. This should make tomorrow's carry-over clear.
- **原因判断**: one short cause statement. Draft only when the cause is visible in the file, such as external blockers, a P0 crowding out lower-priority work, a task being too large, or explicit notes. Leave blank if the likely cause is internal or not recorded.
- **明日调整**: one concrete adjustment for tomorrow's plan. Prefer carrying over unfinished P0 items first, then reducing or splitting lower-priority work.
- **精力**: three slots, each `好`/`一般`/`差`. Accumulates into weekly energy pattern analysis.
- **作息**: actual sleep and wake times. Core tracking data for the Q2 schedule adjustment goal.
- **健身**: free-form (e.g., `有氧 30min` or `否`)
- **明早第一件事**: tomorrow's first concrete action, preferably taken from tomorrow's P0 plan or scheduled event. It should be small enough to start immediately.

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

- Write tomorrow planning tasks based on carry-over P0 items and week priorities.
- Carry over unfinished `P0` items first.
- Limit new tasks. Prefer 1-2 new tasks with clear closure over a long list.

### Review field policy (Variant D, April 2026 onward)

Draft fields the AI can justify from objective sources in the file; leave subjective fields blank.

| Field | AI drafts? | Condition |
|-------|------------|-----------|
| `达成` | Yes | Count parent checkboxes in the day's plan section. Purely mechanical. |
| `今日完成` | Yes | Use checked parent tasks, checked child tasks, and explicit notes. Mention partial progress without marking the parent task complete. |
| `未完成` | Yes | Use unchecked parent tasks and important unchecked child tasks, especially P0 items. |
| `原因判断` | Yes (cautious draft) | Only when the cause is visible in the plan section or notes, e.g. external blocker, task too large, P0 crowding out lower-priority work, multi-day carry-over. Leave blank if the likely cause is emotional, internal, or otherwise not visible in the file. |
| `明日调整` | Yes | Base it on unfinished P0 items and tomorrow's existing plan. Prefer a small concrete adjustment over adding new tasks. |
| `明早第一件事` | Yes | Use tomorrow's scheduled event or first P0 action. Never invent a task unrelated to the plan. |
| `精力（上午/下午/晚上）` | **No** | Subjective. Must come from the user. |
| `作息` | **No** | Actual sleep and wake times. Must come from the user. |
| `健身` | **No** | Actual exercise form and duration. Must come from the user. |

**Empty beats fabricated.** For subjective fields (精力 / 作息 / 健身 and any internal-state cause), leaving blank is always preferable to guessing. These fields are the only feedback-loop data for the user's Q2 energy strategy, and fabricated values permanently corrupt downstream weekly and monthly review analysis. When in doubt, leave blank; the user can fill them manually.

When the AI drafts `原因判断`, the draft must rest on file-visible facts only: which parent tasks were incomplete, how many days they have been carried over, whether a P0 pushed out a P1, whether a task was explicitly noted as skipped in 备注. If the likely cause is something the file cannot show (mood, unplanned meetings, distraction), leave the field blank rather than guess.
