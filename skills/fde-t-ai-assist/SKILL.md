---
name: fde-t-ai-assist
description: "Use when FDE自己用AI|访谈整理|群聊总结|进群只收集|T-12."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, tool, ai-assist]
    trigger: "FDE自己用AI|访谈整理|群聊总结|进群只收集|T-12|转写结构化"
    related_skills: [fde-01-diagnose, fde-02-define, fde-t-observe-card, fde-t-demo-loop]
---

# T-12 AI 辅助 FDE 自己

FDE 用 AI 做访谈整理、群聊总结、Demo 草稿、调研加速。AI 只收集和整理，判断仍由 FDE 与业务方做。进群阶段只收集不解决。

**挂载**：1.2、2.1、4.2。半自动。

## 何时用

- 有群聊 / 访谈录音 / 录屏 / 文档要结构化。
- 要快速出 Demo 草稿。

## 需要的输入

原始材料。进群 2–3 周的材料按「只收集不解决」处理，不要在总结里夹带方案。

## 步骤

1. 转写与结构化。
2. 按角色总结：反复出现的问题、停顿点、需求。
3. FDE（用户）核对与追问——Agent 把待核标出来。
4. 需要时生成 Demo 或方案草稿，标明草稿。
5. 把结构化结果交给对应子流程 skill，判断权不留在本工具。

## 输出

按 [templates/assist-notes.md](templates/assist-notes.md) 写到 `01-diagnose/assist-notes.md` 或当前阶段目录。

## 完成标准

- 事实与推断分开。
- 进群材料没有「已替你解决问题」的表述。
- 待 FDE 核对的列表非空或显式写「已核对」。

## 常见误判

- 把整理当诊断结论。
- 进群就回复业务问题，污染观察。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。
