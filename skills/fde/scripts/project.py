#!/usr/bin/env python3
"""Locate or initialize a Datawhale FDE project beside the skill package."""

import argparse
import shutil
from pathlib import Path


def project_root():
    root = Path(__file__).resolve().parents[3]
    if not (root / "projects/_template/STATE.md").is_file():
        raise SystemExit("找不到项目模板。请按 README 用软链接安装完整仓库。")
    return root / "projects"


def safe_name(value):
    if not value or value in {".", "..", "_template"} or "/" in value or "\\" in value:
        raise argparse.ArgumentTypeError("客户名须为单个目录名，不能包含路径分隔符。")
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["init", "status"])
    parser.add_argument("customer", type=safe_name)
    args = parser.parse_args()

    root = project_root()
    project = root / args.customer
    state = project / "STATE.md"
    if args.action == "init" and not project.exists():
        shutil.copytree(root / "_template", project)
        state.write_text(state.read_text().replace("<客户名>", args.customer))
    if not state.is_file():
        raise SystemExit(f"项目状态不存在：{state}")
    print(state)


if __name__ == "__main__":
    main()
