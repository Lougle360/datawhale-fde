---
name: fde-t-observe-card
description: "Use when 跟岗|观察卡|一天怎么干活|录屏拆SOP|停顿点|T-01."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, tool, observe]
    trigger: "跟岗|观察卡|一天怎么干活|录屏拆SOP|停顿点|T-01|现场观察"
    related_skills: [fde, fde-01-diagnose, fde-t-ai-assist]
---

# T-01 跟岗观察卡

把「一天怎么干活」变成可标注的时间线，找停顿点与隐性判断。只记事实不记结论。

**挂载**：1.2、2.1、3.3、5.5。半自动：从录屏转写 / 群聊导出 / 口述生成草稿，标待本人确认。

## 何时用

- 访谈拿不到细节，或一线说不清隐性经验。
- 上线后再看员工怎么用（5.5）。
- 知识萃取前要事实时间线（3.3）。

## 需要的输入

至少其一：跟岗笔记、录屏转写、群聊导出、员工口述一天。指定岗位与时段。

一线在正式访谈不敢说（NO.13）→ 改录屏或 Agent 进群，不要逼当面讲。

## 步骤

1. 选岗位与时段。
2. 按时间记录每个动作：开什么 / 看什么 / 填什么 / 问谁。
3. 标注四类点：停顿、问人、重复、跨系统搬运。
4. 标注判断点：这里为什么这样选？（只记本人原话，不替他总结成规则。）
5. 回放给本人确认并补例外。未确认前文件标「草稿」。

## 输出

按 [templates/observe-card.md](templates/observe-card.md) 写到 `01-diagnose/observe-card.md`（5.5 则 `05-embed/observe-card.md`）。可据此起草 `sop-draft.md`。

## 完成标准

- 能复述该岗位一天怎么过。
- 四类点至少标出实际存在的。
- 本人确认或明确待确认。

## 常见误判

- 把观察写成结论或方案。
- 只听老板，不看一线。
- 企业自述能力当成现场能力（NO.7）。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。
