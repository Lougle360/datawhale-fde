---
name: fde-03-design
description: "Use when 方案与分工|拆环节|人机分工|门3|阶段3|知识萃取."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, stage, design]
    trigger: "方案与分工|拆环节|人机分工|门3|阶段3|知识萃取|兜底设计"
    related_skills: [fde, fde-t-human-ai-split, fde-t-knowledge-extract, fde-t-calibration-loop, fde-t-demo-loop]
---

# 阶段 3 · 方案与分工

把业务流程拆到环节，决定每一步交给 AI、专业系统、传统算法还是人；把数据和知识准备好。

**门 3**：每个环节有归属；不确定项有人兜底；数据拿得到；部署方式符合 1.4 约束。

**人机边界**：3.2 全自动判定；3.1 / 3.3 / 3.4 / 3.5 / 3.6 半自动。

## 何时用

门 2 已过，或 4.5 回退到方案偏。

## 需要的输入

`02-define/` 第一单与基线、`01-diagnose/sop-draft.md`、`data-ladder.md`、`constraints.md`。

## 步骤

### 3.1 拆环节

有匹配模板则套 [references/m-templates.md](references/m-templates.md) 并标差异；无则从头拆：谁看 / 谁判 / 谁填 / 谁搬 / 谁签。环节说不清 → 3.3 或 `fde-t-demo-loop`。产出 `03-design/step-table.md`。

### 3.2 人机分工

加载 `fde-t-human-ai-split`。产出 `split-table.md`。AI 不够用且人也不想做 → 回 2.3。

### 3.3 知识萃取

依赖老师傅 / 法务 / 优秀运营时加载 `fde-t-knowledge-extract`。可辅 [references/p-03-p-04.md](references/p-03-p-04.md)（知识地图、Spec）。

### 3.4 数据准备

只治理试点范围（`fde-t-scope-narrow`）。阶梯不够 → 先补记录或打通。Key 互斥 → 中转库（P-05）。老系统不让写回 → 旁路呈现。数据根本不存在 → 回 2.3 或先补信息化。

### 3.5 选型与部署

按 [references/p-06-deploy.md](references/p-06-deploy.md)：敏感走本地，复杂推理走云；由轻到重。用 `fde-t-eval-set` 跑一遍候选。不为先进而先进。

### 3.6 兜底与审计

加载 `fde-t-calibration-loop`。一文一图一表容错见 [references/p-07-fault-tolerance.md](references/p-07-fault-tolerance.md)。

## 门 3 检查

[references/gate-3-checklist.md](references/gate-3-checklist.md)。过门 → STATE 阶段 4。

## 完成标准

所有环节有归属；对外节点有兜底人；试点数据可取（或旁路策略已写）。

## 常见失败

把所有事塞给大模型；多智能体互聊丢上下文（NO.4）；跳过萃取（NO.14）；端到端出价（NO.17）。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。
