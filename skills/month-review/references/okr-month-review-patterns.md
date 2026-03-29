# OKR Month Review Patterns

Use this reference when writing a monthly review into the quarterly OKR note under `Plan/年度规划/{YYYY} OKR`.

## 1. Quarter File Resolution

- Map the target month to the matching quarter file such as `2026 第一季度.md`.
- Write into the quarterly OKR note, not into `2026 全年规划.md`.
- Reuse the current quarter file's wording and section order.

## 2. Observed Quarterly OKR Structure

The quarter note uses an objective-first monthly review area as the sole write target.

### Objective-first monthly review area

In the quarterly OKR note, each objective heading is repeated in a lower summary section, and each month is written directly under that repeated objective heading:

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

### Quarter-end summary (季末总结)

When the target month is the last month of a quarter (3月/6月/9月/12月), the quarterly OKR note uses a two-part structure:

1. **整体评价**（`# 🏖️ 整体评价`）：全局总览，放在分项回顾之前
2. **分项回顾**（`# 📋 分项回顾`）：各 Objective 的逐月记录

#### 整体评价结构

```markdown
# 🏖️ 整体评价

## 各 Objective 达成度

评分准则：🔴 0~0.3 / 🟡 0.4~0.6 / 🟢 0.7~1.0

| Objective | 达成度 | 评分 | 评价 |
|---|---|---|---|
| O1：{短标题} | ★★★★☆ | 🟢 0.75 | {一句话，点明哪些 KR 达标/未达标} |
| O2：... | ... | ... | ... |

## Q{N} 核心产出

**工作侧（O1）：**
- ...

**个人侧（O2~O4）：**
- ...

## 做得好的

- ...

## 存在的问题

> [!warning]
> 1. **{问题名}**：{描述}
> 2. ...

## 下个季度需要解决的核心问题

> [!tip]
> - {可执行的行动}
> - ...
```

注意事项：
- 「存在的问题」用 `> [!warning]` callout 突出显示
- 「下个季度需要解决的核心问题」用 `> [!tip]` callout 突出显示
- 「做得好的」和「存在的问题」不要内容重复；前者讲正反馈，后者讲结构性问题
- 不需要单独的「做的不好的」节，「存在的问题」已覆盖

#### 📋 分项回顾结构

```markdown
# 📋 分项回顾

## O1：...

### 1月
{总结段落}

2月重点内容（最多 1–3 条）：
- ...

### 3月
{总结段落}
```

评分准则：🔴 0~0.3（严重不足）/ 🟡 0.4~0.6（部分达标）/ 🟢 0.7~1.0（基本达标或超预期）。根据各 KR 实际完成情况给出 0~1.0 的分数。

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
- Keep per-objective month markers in the file's local style. In the current file that means `### {M}月`.
- Do not write monthly review content into the top KR definition area near the beginning of the file.
- For quarter-end months, write the `# 🏖️ 整体评价` section before `# 📋 分项回顾`. If either section already exists, patch it in place instead of creating duplicates.

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
