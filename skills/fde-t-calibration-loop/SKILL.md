---
name: fde-t-calibration-loop
description: "Use when 人工校准|回填|低置信度|人审队列|T-08."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, tool, calibration]
    trigger: "人工校准|回填|低置信度|人审队列|T-08|边用边准"
    related_skills: [fde-03-design, fde-04-mvp, fde-05-embed, fde-t-eval-set]
---

# T-08 人工校准回填环

AI 初筛 + 人确认 + 修正回填，边用边准。只让人审低置信度部分；修正必须回到样本 / 规则，不然人永远在审。

**挂载**：3.6、4.3、5.5、6.1。半自动：设计环与阈值，记录回填，不代替人审。

## 何时用

- 设计兜底（3.6）。
- 真实数据实验（4.3）。
- 上线陪跑与效果监控。

## 需要的输入

AI 节点清单、是否能输出置信度与依据、评估样本集（可调 `fde-t-eval-set`）。

## 步骤

1. 每个 AI 输出必须带：来源、置信度、判断依据。
2. 设阈值。≥ 阈值自动通过；< 阈值进人工确认队列。
3. 人修正 / 确认。
4. 修正样本回填：评估集 / 规则 / 提示词。
5. 更新阈值与规则。
6. 溯不回原始数据的问题不让答。

## 输出

按 [templates/calibration.md](templates/calibration.md) 写到 `03-design/calibration.md`，运行记录可追加到 `04-mvp/` 或 `05-embed/`。

## 完成标准

- 每个对外 AI 节点有阈值和兜底人。
- 回填去向写清（样本集 / 规则 / 提示词）。
- 人不是在审 100% 件。

## 常见误判

- 人审全部，校准环不回填。
- 无来源仍自动放行。
- 加工具型也省略本环（门 1–3 可压缩，本环不能省）。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。
