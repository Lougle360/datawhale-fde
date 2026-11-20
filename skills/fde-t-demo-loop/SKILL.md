---
name: fde-t-demo-loop
description: "Use when 快速Demo|往返|阶段性产出|逼出需求|T-06."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, tool, demo]
    trigger: "快速Demo|往返|阶段性产出|逼出需求|T-06|第一版不求满分"
    related_skills: [fde-03-design, fde-04-mvp, fde-05-embed, fde-t-ai-assist]
---

# T-06 快速 Demo 往返

用阶段性产出逼出真实需求，替代长篇需求文档。第一版不求满分；反馈必须落到指定文档；往返十几次是正常。

**挂载**：3.1、4.2、5.2、5.5。半自动：出 Demo 说明与反馈档，人拿去给客户看。

## 何时用

- 环节说不清，用 Demo 逼隐藏步骤（3.1）。
- MVP 细节模糊（4.2）。
- 修改后回到关键人（5.2 / 5.5）。

## 需要的输入

客户给的一部分真实输入 + 环节表或 SOP。没有真实输入就先要，不要用假数据冒充往返。

## 步骤

1. 用一部分输入快速做出可看可点的东西（可调 `fde-t-ai-assist`）。
2. 明确给谁看：客户 + 一线，不是只给 IT。
3. 问：是这个意思？操作顺？
4. 否 → 反馈写进指定文档，再做下一版。
5. 是 → 记入「已确认需求」，可进 4.3。
6. 反复多轮仍对不上 → 回 2.1，不要在 Demo 里空转。

## 输出

按 [templates/demo-log.md](templates/demo-log.md) 写到 `04-mvp/demo-log.md`（3.1 用 `03-design/demo-log.md`）。

## 完成标准

- 每一轮有输入、产出、看的人、原话反馈。
- 反馈在文档里，不在聊天里丢失。

## 常见误判

- Demo 看起来好但没人真用（NO.14）。
- 第一版求 100 分导致不出活。
- 把能跑当成能落地（NO.16）。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。
