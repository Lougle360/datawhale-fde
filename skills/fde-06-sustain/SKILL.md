---
name: fde-06-sustain
description: "Use when 沉淀扩展|效果监控|二期|阶段6|企业自己搭工具."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, stage, sustain]
    trigger: "沉淀扩展|效果监控|二期|阶段6|企业自己搭工具|如实表述|黑客松"
    related_skills: [fde, fde-t-baseline, fde-t-scene-scorecard, fde-t-knowledge-extract, fde-t-scope-narrow]
---

# 阶段 6 · 沉淀与扩展

把效果持续证明下去；把知识、Skill、SOP、团队留在企业；FDE 自己也留下方法和组件；识别二期。

**阶段出口**：客户开始自己提需求、自己搭小工具；效果按基线持续可见；FDE 方法库有新增。

**人机边界**：6.1 半自动报告；6.4 全自动重排场景；6.2 / 6.3 半自动清单。

## 何时用

门 5 已过，或客户主动提二期。

## 需要的输入

`02-define/baseline.md`、运行数据、本项目走过的六步与回退记录。

## 步骤

### 6.1 效果持续监控与如实表述

加载 `fde-t-baseline`。已证明 / 尚待验证分开写。下降 → 5.5；消失 → 视为未落地，回 4.5。对外只引用已证明项（NO.20、NO.24）。产出 `06-sustain/effect-report.md`。

### 6.2 企业能力沉淀

文档化 → 流程化 → 人（培训 / 标兵 / 编制）→ 黑客松（[references/p-11-hackathon.md](references/p-11-hackathon.md)）。可调 `fde-t-knowledge-extract`。无人接手 → 5.4。退出：遇到新问题先自己试。

### 6.3 FDE 自身沉淀

复盘四问：哪步没工具、哪个门虚设、哪个子流程被跳过、改造后流程能否抽成 M-xx。标准化方法，不急于标准化产品。产出 `retro.md`。目标：同类项目 100% → 80% → 60% 工时（NO.5）。

### 6.4 二期识别与扩面

客户新需求 + 上一期下一层问题，用 `fde-t-scene-scorecard` 重排；同场景扩范围用 `fde-t-scope-narrow`；新场景回阶段 2 走门 2。都不成立则收尾并约定回访（防 NO.22 权限被撤）。

## 出口检查

[references/gate-exit-checklist.md](references/gate-exit-checklist.md)。二期启动则 STATE 当前阶段改 2，门 2 起重。

## 完成标准

有效果报告；企业侧有接手人或书面缺口；方法库复盘已写；二期有排序或收尾约定。

## 常见失败

东西做完钱到账人撤走（NO.8）；交付后权限移除（NO.22）；一个项目急着包装成标准产品（NO.20）。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。
