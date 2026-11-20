# Datawhale FDE

基于 Datawhale《FDE落地100案例》首批 24 案整理的《FDE 落地六步法》，做成可调用的 FDE 项目 Skill。它包含 1 个项目路由、6 个阶段 Skill 和 12 个循环工具 Skill。路由读取项目的 `STATE.md`，找到当前未通过的关门条件，再调用对应阶段并把结果记录在同一项目目录。

## 六个阶段

| 阶段 | 目标 | 下一步依据 |
|---|---|---|
| 进场诊断 | 观察真实任务，盘点干系人、系统和数据 | 有一份由一线核对的现状 SOP |
| 问题定义 | 追根因、选择第一单、建立价值基线 | 问题价值、数据来源和业务确认人明确 |
| 方案与分工 | 拆业务环节，安排 AI、系统、算法与人的职责 | 每个环节有负责人，异常有人接管 |
| 窄 MVP 验证 | 在限定范围用真实数据对比现状 | 业务人员使用并确认结果，留下实测证据 |
| 嵌入与推广 | 接回原有工作入口，陪跑并逐步扩大范围 | 员工持续使用，工作流程可观察和修订 |
| 沉淀与扩展 | 监控效果、移交能力、复盘方法与下一期 | 客户侧能接手，价值和下一步都有记录 |

项目会根据证据回退。若发现问题选错，回到定义阶段；方案或数据不足，回到设计阶段。完整分工和方法在 [总入口](skills/fde/SKILL.md) 与 [六步法总览](methods/00-总览.md)。

## 安装

```sh
git clone https://github.com/Lougle360/datawhale-fde.git
cd datawhale-fde
mkdir -p ~/.agents/skills
for skill in skills/*; do ln -s "$(pwd)/$skill" ~/.agents/skills/"$(basename "$skill")"; done
```

保持仓库目录在原位置，软链接会让 Skill 找到本仓库的项目模板和方法文件。新会话打开后可说“用 `fde` 开一个 FDE 项目，客户叫 XX”，也可直接调用 `fde-t-baseline` 等工具。

## 项目目录

`projects/_template/` 是新项目模板。路由可运行 `python3 skills/fde/scripts/project.py init XX` 建立 `projects/XX/`；之后用 `status XX` 返回状态文件位置。每个项目有 `STATE.md`、`log.md` 和六个阶段目录。实际客户材料仅保留在本机项目目录，默认不会被 Git 跟踪。示例见 [虚构 ERP 项目](examples/demo-erp/STATE.md)。

## 资料和使用状态

`methods/` 保存九份《FDE 落地六步法》方法文档，供各阶段回查；`skills/*/references/` 保存对应的案例、检查表和专属方法。示例项目采用虚构客户输入，真实客户的收益与门状态需以项目证据判断。本 Skill 套件依据 Datawhale 案例资料整理，并核对了引用与安装路径。
