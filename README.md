# AI Workspace

个人 AI 工具链配置仓库，集中管理 Claude Code / Coco 的 Skills、Sub-agents 和相关资源。

## Skills

### 规划与复盘

| Skill | 说明 |
|-------|------|
| **daily-review** | 每日复盘与次日规划，自动分析完成情况并更新 Obsidian 月度规划文件中的日级区块 |
| **weekly-review** | 周复盘与下周规划，汇总本周里程碑与风险，更新周级区块 |
| **month-review** | 月度复盘与下月规划，将月度进展映射到季度 OKR，更新月级回顾区域 |

### Obsidian 工具

| Skill | 说明 |
|-------|------|
| **obsidian-cli** | 通过 CLI 与 Obsidian Vault 交互：读写笔记、搜索、管理任务与属性，支持插件开发调试 |
| **obsidian-markdown** | Obsidian 风格 Markdown 编辑：wikilinks、embeds、callouts、properties 等语法支持 |
| **obsidian-bases** | 创建和编辑 Obsidian Bases（.base 文件），支持视图、筛选、公式和汇总 |
| **json-canvas** | 创建和编辑 JSON Canvas 文件（.canvas），支持节点、连线、分组 |
| **mind-recorder** | 随手记录想法、灵感到 Obsidian DailyNote |

### 通用工具

| Skill | 说明 |
|-------|------|
| **defuddle** | 从网页提取干净的 Markdown 内容，去除导航和杂乱元素，节省 token |
| **skill-creator** | 创建、修改和优化 Skills，支持 eval 测试和性能基准分析 |

## 目录结构

```
ai-workspace/
├── skills/                # 所有 Skills
│   ├── daily-review/      # 每日复盘
│   ├── weekly-review/     # 周复盘
│   ├── month-review/      # 月度复盘
│   ├── obsidian-cli/      # Obsidian CLI 交互
│   ├── obsidian-markdown/ # Obsidian Markdown 语法
│   ├── obsidian-bases/    # Obsidian Bases
│   ├── json-canvas/       # JSON Canvas
│   ├── mind-recorder/     # 想法记录
│   ├── defuddle/          # 网页内容提取
│   └── skill-creator/     # Skill 开发工具
└── log/                   # 运行日志
```

## 使用方式

Skills 通过 Claude Code 的 skill 机制加载，放置在对应工具的 skills 目录下即可自动识别。

## License

MIT
