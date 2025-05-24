#!/usr/bin/env python3

from i3tools._message import i3msg
import sys


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ["prev", "next"]:
        print("Usage: i3ws <prev|next>", file=sys.stderr)
        sys.exit(1)

    workspaces = i3msg("get_workspaces", None)

    i = 0
    for ws in workspaces:
        if i >= len(workspaces) - 1:
            i = -1

        change_to = (i - 1) if sys.argv[1] == "prev" else (i + 1)

        if ws["focused"]:
            i3msg(None, "workspace {0}".format(workspaces[change_to]["name"]))

        i += 1
