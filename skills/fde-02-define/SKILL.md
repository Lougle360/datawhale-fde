---
name: fde-02-define
description: "Use when 问题定义|追根因|选第一单|门2|阶段2|抱怨追到钱."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, stage, define]
    trigger: "问题定义|追根因|选第一单|门2|阶段2|抱怨追到钱|价值链|ROI定义"
    related_skills: [fde, fde-t-why-chain, fde-t-scene-scorecard, fde-t-baseline, fde-t-stakeholder-map, fde-t-observe-card]
---

# 阶段 2 · 问题定义

把模糊抱怨追到根因，挂到收入 / 成本 / 风险上，选出第一单。

**门 2**：能说出「这个问题解决后一年值多少钱、数据从哪来、最后谁确认」，并且业务部门自己愿意做。

**人机边界**：2.1 半自动（出根因草稿，人确认）；2.2 / 2.3 / 2.4 全自动判断（缺证据就停）；2.5 人做、agent 备料（会前话术与对齐表）。

## 何时用

- 路由判定当前阶段为 2，或门 1 已过、门 2 未过。
- 用户甩来一句话需求：「要 AI 化」「ERP 不好用」「把系统打通」。

## 需要的输入

优先读 `projects/<客户>/`：

- `STATE.md`
- `01-diagnose/sop-draft.md`（没有则 2.1 可能回退到 1.2）
- `01-diagnose/stakeholders.md`、`01-diagnose/data-ladder.md`

没有项目目录 → 先走 `fde` 路由建 `projects/<客户>/`。

## 步骤

按 2.1 → 2.5 顺序。加工具型可压缩深度，但不跳过。

### 2.1 表层需求到根因（半自动）

1. 读客户原话 + SOP。
2. 加载 `fde-t-why-chain`，先追到「哪一步、谁做、多久一次」。
3. 落不到 SOP 某一步 → 停，回 1.2，调用 `fde-t-observe-card` / `fde-t-ai-assist`。
4. 写出具体问题，按 [templates/root-cause.md](templates/root-cause.md) 存 `02-define/root-cause.md`，标「待人确认」。

### 2.2 业务价值链还原（全自动结构，终点需人认）

1. 继续用 `fde-t-why-chain`：然后呢 → 再然后 → 终点是否为收入 / 成本 / 风险 / 关键人时间。
2. 链断或终点不是这四个 → 记录后放下，回 2.1 换问题。
3. 写出 [templates/value-chain.md](templates/value-chain.md) → `02-define/value-chain.md`。

例（NO.8，仅作结构参考）：找不到 → 重录 → 数据脏 → 买错 → 积压 → 报废 → 损失。

### 2.3 场景筛选（全自动）

候选 ≥ 2 时加载 `fde-t-scene-scorecard`。可辅以 `fde-t-human-ai-split` 粗判要不要 AI。产出 `02-define/scorecard.md`。

### 2.4 ROI 与效果基线（全自动填表，数字不编）

加载 `fde-t-baseline`。现状没有数字 → 安排采样，不假装门 2 已过。产出 `02-define/baseline.md`。

### 2.5 利益相关方共同确认（人做、agent 备料）

涉及多部门时加载 `fde-t-stakeholder-map`：

1. 会前单聊话术（化解没在会上说的顾虑）。
2. 会上确认项：解决什么 / 是否真需要 / 先后顺序。
3. 边界写字：谁投入、成功标准、AI 出错谁判断谁处理。
4. 某部门不配合 → 标记「3.6 留容错」，不少场景就卡死整条链（NO.4）。

产出 `02-define/alignment.md`。

## 门 2 检查

按 [references/gate-2-checklist.md](references/gate-2-checklist.md) 逐项打勾。全过才改 `STATE.md`：

- 当前阶段 → 3
- 门 2 → 过 + 日期
- 产出索引补上 02-define 文件
- 追加 `log.md`

未过：写清缺哪一项，不要进阶段 3。

## 完成标准

- `root-cause.md` 定位到 SOP 具体环节。
- `value-chain.md` 终点是四个之一，且业务方认可或标待确认。
- `scorecard.md` 有第一单或破冰建议。
- `baseline.md` 有确认人和数据来源。
- 多部门项目有 `alignment.md`。

## 常见失败

- 拿着锤子找钉子（NO.8）。
- 需求列表变功能列表。
- 为 AI 而 AI（NO.20 生图反例）。
- 门 1 的 SOP 还是访谈稿，2.1 会空转。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。

行业模板对照见 [references/m-templates.md](references/m-templates.md)，本阶段只对号，不拆环节（拆环节是 3.1）。
