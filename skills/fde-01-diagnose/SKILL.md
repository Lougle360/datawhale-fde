---
name: fde-01-diagnose
description: "Use when 进场诊断|跟岗|数据盘点|门1|阶段1|现场SOP."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, stage, diagnose]
    trigger: "进场诊断|跟岗|数据盘点|门1|阶段1|现场SOP|合规摸底"
    related_skills: [fde, fde-t-stakeholder-map, fde-t-observe-card, fde-t-ai-assist]
---

# 阶段 1 · 进场诊断

看清企业每天怎么工作、数据在哪一档、谁是干系人，先把技术往后放。

**门 1**：拿到一份现场还原的 SOP（谁做 / 输入 / 输出 / 判断点 / 耗时），不是会议室访谈稿。

**人机边界**：1.1 人做、agent 备料；1.2 半自动（观察卡草稿）；1.3 / 1.4 半自动（出盘点表与约束清单，人补事实）。

## 何时用

- 新项目，或门 1 未过。
- 2.1 落不到 SOP，被退回补观察。

## 需要的输入

`projects/<客户>/STATE.md`、组织架构、系统清单。没有项目目录先走 `fde` 路由。

## 步骤

### 1.1 干系人识别与分层访谈

加载 `fde-t-stakeholder-map`。三层都谈过，找到执行一号位。不通则项目不启动。产出 `01-diagnose/stakeholders.md`。

### 1.2 现场跟岗观察

加载 `fde-t-observe-card`。方式：能到现场跟一天；远程或一线有压力则录屏；长期沉浸则 Agent 进群 2–3 周（`fde-t-ai-assist`，只收集不解决）。回放本人确认。产出 `observe-card.md` + `sop-draft.md`。

### 1.3 系统与数据盘点

与 1.2 并行。按 [references/p-01-data-ladder.md](references/p-01-data-ladder.md)：

- 纸 / Excel / 微信 → 信息化未完成，先补记录。
- 系统有但互不通 → 数据化未完成，需数仓 / 中转 / 口径对齐。
- 统一数仓 → 可直接智能化。

每类数据写：位置、口径、可导出、可写回。信息化未完成 → 阶段 3 的 3.4 先补基础，不直接上模型。产出 `data-ladder.md`。

### 1.4 环境与合规摸底

跨境、央国企、金融、上市公司、或需在客户电脑运行时必做。按 [references/p-02-compliance.md](references/p-02-compliance.md) 出约束清单，并启动权限 / 数据申请。产出 `constraints.md`。

## 门 1 检查

按 [references/gate-1-checklist.md](references/gate-1-checklist.md)。过门后更新 STATE：当前阶段 2，门 1 过 + 日期。

## 完成标准

- SOP 能复述一天且被本人确认，或明确待确认清单。
- 能回答：AI 要的数据今天在不在、在谁手里、拿不拿得出。
- 执行一号位已点名。

## 常见失败

- 只听老板。
- 一线正式访谈不敢说（NO.13）。
- 企业自述能力 ≠ 现场真实能力（NO.7）。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。
