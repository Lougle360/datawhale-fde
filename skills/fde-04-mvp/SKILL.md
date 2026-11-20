---
name: fde-04-mvp
description: "Use when 窄MVP|真实数据验证|门4|阶段4|Demo往返|问题回退."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, stage, mvp]
    trigger: "窄MVP|真实数据验证|门4|阶段4|Demo往返|问题回退|业务方确认"
    related_skills: [fde, fde-t-scope-narrow, fde-t-demo-loop, fde-t-eval-set, fde-t-baseline, fde-t-why-chain]
---

# 阶段 4 · 窄 MVP 验证

在一个足够小、足够真实、能闭环的范围里，用真实数据跑通，让业务人员亲眼看到有效。

**门 4**：业务人员在真实数据上用过并说「有效」；与基线对比有数字；问题定义与方案没有被推翻。

**人机边界**：4.1 / 4.5 全自动建议；4.2 / 4.3 / 4.4 半自动（确认必须来自业务方）。

## 何时用

门 3 已过，或待回退项指向 4.x。

## 需要的输入

`03-design/` 环节与分工、`02-define/baseline.md`、试点真实数据。

## 步骤

### 4.1 范围收敛

加载 `fde-t-scope-narrow`。产出 `04-mvp/mvp-scope.md`。

### 4.2 Demo 往返

加载 `fde-t-demo-loop`（可辅 `fde-t-ai-assist`）。对不上多轮 → 回 2.1。产出 `demo-log.md`。

### 4.3 真实数据实验

加载 `fde-t-eval-set` + `fde-t-calibration-loop`。指标不达：样本不够 → 3.4；规则 / 提示词 → 3.3 / 3.5；分工不对 → 3.2。产出 `experiment.md`。

### 4.4 基线对比与业务方确认

加载 `fde-t-baseline`。业务人员亲口说有效才算，FDE 不得自行宣布。不认 → 4.5。

### 4.5 问题回退

加载 `fde-t-why-chain` 分类，必要时 `fde-t-human-ai-split` 重判。

- 不是这个问题 → 2.1 / 2.2
- AI 做不好 → 3.2
- 数据不行 → 3.4
- 范围太大 → 4.1
- 不愿用 → 5.4 / 2.5

写入 `rollback.md` 与 STATE 待回退项，并记 6.3。不在阶段 4 空转。

## 门 4 检查

[references/gate-4-checklist.md](references/gate-4-checklist.md)。过门 → STATE 阶段 5。

## 完成标准

过程指标达约定线；业务结果有对比；有业务方原话确认。

## 常见失败

接全部系统（NO.4）；Demo 好没人用（NO.14）；能跑当能落地（NO.16）。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。
