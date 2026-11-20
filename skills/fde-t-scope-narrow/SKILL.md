---
name: fde-t-scope-narrow
description: "Use when 收敛范围|MVP边界|缩到一个点|T-11."
version: 1.0.0
author: FDE落地六步法
license: MIT
metadata:
  hermes:
    tags: [fde, tool, scope]
    trigger: "收敛范围|MVP边界|缩到一个点|T-11|一个部门一条线"
    related_skills: [fde-04-mvp, fde-03-design, fde-06-sustain]
---

# T-11 收敛范围法

把「全公司」缩到「一个能一两周闭环的点」。缩到数据能治理干净、端到端能闭环为止；扩面时反向逐步加。

**挂载**：4.1、3.4（只治理试点数据）、6.4。全自动建议边界，人拍板。

## 何时用

- 进入阶段 4。
- 数据治理范围过大。
- 二期扩面要反向逐级加。

## 需要的输入

第一单场景、数据盘点。

## 步骤

1. 全量 → 一个部门 / 区域。
2. 再 → 一个单元 / 一条产品线 / 几个门店。
3. 只挑 1–2 条业务流，只回答 1 个问题。
4. 问：范围内数据一两周能干净？数据能进、结果能出、结论能进会议？
5. 否 → 继续缩。是 → 写下 MVP 边界。
6. 扩面：按相反顺序逐级加，不一次铺开。

## 输出

按 [templates/mvp-scope.md](templates/mvp-scope.md) 写到 `04-mvp/mvp-scope.md`。3.4 可引用同一边界。

## 完成标准

- 边界具体到部门 / 产品线 / 门店 / 问题各至少一个限定。
- 写明闭环三件：进、出、进会。

## 常见误判

- 一开始接全部系统，陷入永远做不完的数据工程（NO.4）。
- 范围仍是「全公司 AI 化」。

## 案例参考

只引用 [references/cases.md](references/cases.md)。编号锁定 NO.1–NO.24，禁止编造。
