---
name: fde-t-knowledge-extract
description: "Use when 知识萃取|岗位说明书|老师傅|隐性规则|T-10."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, tool, knowledge]
    trigger: "知识萃取|岗位说明书|老师傅|隐性规则|T-10|例外清单"
    related_skills: [fde-03-design, fde-06-sustain, fde-t-observe-card]
---

# T-10 知识萃取 / 岗位说明书

把老师傅、法务、优秀运营的隐性判断变成显性规则。让本人「给 AI 写岗位说明书」最有效；翻历史产出物反推；例外清单必须有。

**挂载**：3.3、6.2。半自动：出问卷并整理答卷，本人确认前不算完成。

## 何时用

- 环节依赖隐性经验。
- 企业要把知识留在组织（6.2）。

## 需要的输入

关键人、历史产出物（合同、报价单、文案、图纸）。本人不愿交 → 先 5.4 解决「替代 vs 助手」，再回来。

## 步骤

1. 找到真正做事的人。
2. 请本人写：输入 / 输出 / 何时判断 / 可直接执行的规则 / 需要的上下文。
3. 翻历史产出物，反推隐含规则。
4. 整理为字段 / 规则 / 框架 / 例外。
5. 本人确认「我就是这么判断的」。不确认就回步骤 2。

## 输出

按 [templates/job-spec.md](templates/job-spec.md) 写到 `03-design/job-spec.md`。可进入知识库 / 流程节点 / 评估集。

## 完成标准

- 有例外清单。
- 本人确认或明确拒绝及下一步（5.4）。
- 没有把 Agent 猜的规则写成「已确认」。

## 常见误判

- 跳过萃取让模型自己理解业务（NO.14）。
- 只问管理者不问做事的人。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。
