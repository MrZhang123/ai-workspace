# OKR Month Review Patterns

Use this reference when writing a monthly review into the quarterly OKR note under `Plan/年度规划/{YYYY} OKR`.

## 1. Quarter File Resolution

- Map the target month to the matching quarter file such as `2026 第一季度.md`.
- Write into the quarterly OKR note, not into `2026 全年规划.md`.
- Reuse the current quarter file's wording and section order.

## 2. Observed Quarterly OKR Structure

The current quarter note contains two month-review layers. The objective-first layer is now the primary write target.

### Layer A: Objective-first monthly review area

In the latest `2026 第一季度.md`, the quarter note repeats the objective headings after the month overview block and writes each month directly under that repeated objective heading:

```markdown
## O1：...

### 1月

{本月总结}

2月重点内容（最多 1–3 条）：

- ...

### 2月
```

Important implications:

- There is no `### 月度复盘` wrapper in the current file.
- Month headings are currently written as `### 1月`, `### 2月`, not `**1月**`.
- Empty placeholders such as `### 2月` may already exist. Fill them instead of creating duplicates.
- Reuse the repeated objective headings in this lower review area rather than writing under the top KR definition area.

### Layer B: Quarter-level month summary

At the bottom of the quarter note there is a monthly overview block:

```markdown
# 🗓️ 2026.01 月度复盘与下月重点

## 进度总览（事实）
- 工作：...
- 个人：...

## 本月里程碑（最多 3–6 条）
- ...

## 模式与偏差（洞察）
- ...

## 下月重点（2 月）
详见各 Objective 下的「### 月度复盘」模块（每个 O 给出 1–3 条可验收重点）。
```

Update both layers for the target month, but prioritize Layer A as the main review output.

## 3. Objective Mapping

Use the quarter file's objective meaning as the source of truth. For the current 2026 Q1 file, the dominant mapping is:

- `O1`: 工作主线、业务理解、AI 在真实工作中的使用、技术/业务沉淀
- `O2`: 投资、公司分析、验证清单、分析框架复盘
- `O3`: 英语、写作、阅读节奏与长期输出
- `O4`: 睡眠、运动、精力管理、身体与个人运行系统

If one task could map to multiple objectives, choose the dominant intent and avoid duplicating the same evidence under multiple O sections.

## 4. Update Rules

- If the target month already exists under the repeated objective heading, patch that month instead of appending a second `### {M}月`.
- If the file already contains an empty month placeholder such as `### 2月`, fill that placeholder in place.
- If the target month already has a quarter-level summary block, patch that block instead of creating a second `# 🗓️ YYYY.MM 月度复盘与下月重点`.
- Keep per-objective month markers in the file's local style. In the current file that means `### {M}月`.
- Keep the quarter-level summary heading as `# 🗓️ YYYY.MM 月度复盘与下月重点`.
- Keep `下月重点` in the overview block short and point back to the objective sections when the detail already lives there.
- Do not write monthly review content into the top KR definition area near the beginning of the file.

## 5. Counting Rules

- Separate work and personal metrics in the overview block.
- Count parent tasks as the primary unit for headline completion metrics.
- If a parent task owns child checkboxes, use the parent task in top-line completion rates and mention child progress only as supporting detail.
- Keep `P0`, `P1`, and untagged tasks separate when the data supports it.
- Ignore malformed checklist lines and explanatory bullets without checkboxes.

## 6. Preferred Output

Prioritize:

- 3-6 milestone-style outputs for the month
- 1-3 structural patterns or breakpoints
- 1 short month summary paragraph per objective
- 1-3 next-month actions per objective that are concrete and checkable

Avoid:

- replaying the full task list
- writing vague promises such as `继续努力`
- inventing new objective names or changing the existing OKR taxonomy
