---
name: fde-t-why-chain
description: "Use when 追问链|五问|根因|然后呢|价值链|T-03."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, tool, why-chain]
    trigger: "追问链|五问|根因|然后呢|价值链|T-03|表层需求"
    related_skills: [fde-02-define, fde-04-mvp]
---

# T-03 追问链

从一句抱怨追到根因与财务终点。追到收入 / 成本 / 风险 / 关键人时间之一才停。

**挂载**：2.1、2.2、4.5。全自动：根据已有信息往下追，缺答就列待问，不编造中间环节。

## 何时用

- 客户给一句话需求。
- 要把具体问题接到钱上。
- MVP 失败，追失败原因（4.5）。

## 需要的输入

原话。有 SOP 更好。4.5 时输入失败现象。

## 步骤

1. 原话 → 具体在哪一步？谁做？多久一次？
2. 然后会发生什么？再然后？直到终点是四个之一。
3. 反向三问：解决后一年值多少？数据从哪来？谁确认？
4. 4.5 时改问失败属哪类：不是这个问题 / AI 做不好 / 数据不行 / 范围太大 / 不愿用，对应回 2.1、3.2、3.4、4.1、5.4。

## 输出

按 [templates/why-chain.md](templates/why-chain.md) 写到 `02-define/why-chain.md`。结论同步进 `root-cause.md` 与 `value-chain.md`。4.5 写到 `04-mvp/rollback.md`。

## 完成标准

- 问题落到某一步，或明确回 1.2。
- 终点是四个之一，或明确「不值得做 AI」。
- 没有编造未证实的中间环。

## 常见误判

- 停在「系统不好用」。
- 把功能点当成根因。
- 用案例的链（NO.8 报废）套到无关客户上。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。
