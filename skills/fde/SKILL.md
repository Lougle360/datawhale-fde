---
name: fde
description: "Use when FDE落地|六步法|进场|AI落地项目|从哪一步开始|开一个FDE项目."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, router]
    trigger: "FDE落地|六步法|进场|AI落地项目|从哪一步开始|开一个FDE项目|FDE agent"
    related_skills: [fde-01-diagnose, fde-02-define, fde-03-design, fde-04-mvp, fde-05-embed, fde-06-sustain]
---

# FDE 路由

读项目状态，判断在哪个阶段、哪道门没过，再加载对应阶段 skill。本 skill 不做业务分析。

项目根目录是本仓库的 `projects/<客户名>/`。从本 Skill 的实际文件位置找到仓库根目录，软链接安装时先解析链接目标。运行 `python3 <仓库根目录>/skills/fde/scripts/project.py init <客户名>` 新建项目，或用同一脚本的 `status <客户名>` 定位现有状态；不要依赖当前工作目录。

方法来源在本仓库的 [methods/](../../methods/00-总览.md)。

## 何时用

- 用户说「做一个 FDE 项目」「从哪一步开始」「继续上次的客户」。
- 不确定当前该调哪个阶段 / 工具 skill。

## 需要的输入

- 客户名（没有就问）
- 可选：项目类型（加工具型 / 小流程型 / 大框架型）、一句需求

## 步骤

1. 解析客户名，读 `projects/<客户>/STATE.md`。
2. **没有 STATE.md**：
   - 调用 `python3 <仓库根目录>/skills/fde/scripts/project.py init <客户名>`，从 `projects/_template/` 建立项目；已有同名项目时直接读取状态
   - 填客户名、项目类型（未指定则先标「待定」，用第 4 节三档规则问一句）
   - 当前阶段 = 1，五道门都未过
   - 加载 `fde-01-diagnose`
3. **有 STATE.md**：找第一道未过的门。
   - 门 1 未过 → `fde-01-diagnose`
   - 门 2 未过 → `fde-02-define`
   - 门 3 未过 → `fde-03-design`
   - 门 4 未过 → `fde-04-mvp`
   - 门 5 未过 → `fde-05-embed`
   - 五道门都过 → `fde-06-sustain`（监控 / 沉淀 / 二期）
4. 若 `STATE.md` 有「待回退项」，优先按回退去向加载，不按门顺序往前冲。
5. 用户点名某个工具（人机分工、评分卡、基线等）→ 直接加载对应 `fde-t-*`，做完把产出写回当前阶段目录，并在 `log.md` 记一笔。
6. 阶段 skill 结束后：更新门状态、当前阶段、产出索引，追加 `log.md`。**不要替用户改门为「过」，除非该阶段 checklist 全勾。**

## 三档规模（不跳阶段，只压缩深度）

- **加工具型**（NO.13 月检生成、NO.14 自助小 Agent）：六步一天走完；重点 3.2 + T-08；门 1–3 可口头确认但必须写进 STATE。
- **小流程型**（NO.10 对账、NO.9 报销、NO.22 库存）：六步完整走，套一张 M-xx，改一条链路。
- **大框架型**（NO.14 国企整体、NO.18 上市公司、NO.7 研发转型）：多子流程并行；1.3 先判数据阶梯；5.4 组织配套必做。

## 门一览

| 门 | 过的标准 |
|---|---|
| 1 | 现场还原的 SOP，不是访谈稿 |
| 2 | 问题能算钱，数据有来源，有人确认 |
| 3 | 每个环节写清 AI / 系统 / 算法 / 人谁负责，不确定项有人兜底 |
| 4 | 业务人员在真实数据上用过并认可 |
| 5 | 进入原工作流，不另开 AI 入口 |

回退：4 失败且问题定义偏 → 阶段 2；方案偏 → 阶段 3；5 推广受阻属组织问题 → 阶段 3 或 5.4；6 的二期新需求 → 阶段 2。

## 输出

- 新建或更新 `STATE.md`（格式见 `projects/_template/STATE.md`）
- `log.md` 一行：日期、动作、产出文件、下一跳

## 完成标准

- 用户知道下一步加载哪个阶段 skill。
- 项目目录存在且 STATE 与真实产出一致。

## 常见误判

- 跳阶段。
- 无 SOP 就进问题定义。
- 把案例效果写进本项目基线。
- 一次会话想把六步做完（大框架型做不到）。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。
挂载矩阵见 [references/tool-matrix.md](references/tool-matrix.md)。
