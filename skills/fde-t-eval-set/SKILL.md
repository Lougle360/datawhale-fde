---
name: fde-t-eval-set
description: "Use when 评估样本集|测试集|回归|同问同答|T-09."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, tool, eval]
    trigger: "评估样本集|测试集|回归|同问同答|T-09|达标线"
    related_skills: [fde-03-design, fde-04-mvp, fde-t-calibration-loop]
---

# T-09 评估样本集

选型、实验、迭代都拿同一套样本跑，防止「感觉变好了」。含正例、负例、异常例；标注答案来自业务方；每次修改后全量回归。

**挂载**：3.5、4.3、5.5。半自动：抽样清单与标注模板，标准答案必须业务方给。

## 何时用

- 技术选型时跑一遍候选方案（3.5）。
- 真实数据实验（4.3）。
- 陪跑每次改动后回归（5.5）。

## 需要的输入

真实数据抽样权限、业务方标注人、约定指标与达标线。

## 步骤

1. 从真实数据抽样，覆盖正例 / 负例 / 边界 / 异常。
2. 业务方标注标准答案。Agent 不得代标后当标准。
3. 定指标与达标线（例：NO.1 解析约 95%、召回 ≥ 80%；NO.16 同问同答稳定）。
4. 每次改动后全量回归。
5. 不达标 → 补样本或回 3.3 / 3.4 / 3.5 / 3.2。

## 输出

按 [templates/eval-set.md](templates/eval-set.md) 写到 `04-mvp/eval-set.md`（选型阶段可用 `03-design/eval-set.md`）。样本明细可另表，本文件只留索引与达标线。

## 完成标准

- 四类样本都有或写明缺哪类、何时补。
- 标注人是业务方。
- 达标线与客户共同约定，不是 FDE 单方面。

## 常见误判

- 只用正例。
- 用 Demo 假数据当评估集。
- 改了提示词不回归。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。
