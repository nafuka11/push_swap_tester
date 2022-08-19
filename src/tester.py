from __future__ import annotations

import os
import subprocess
from collections import Counter
from pathlib import Path
from statistics import median_high
from typing import Any

from src import const
from src.exception import CommandNotFoundError, ExecutePermissionError
from src.gen_int import generate_args
from src.print import print_colored
from src.tester_result import TesterResult


class Tester:
    def __init__(self, **kwargs: Any) -> None:
        dir = kwargs.get("dir") or Path(const.PROJECT_DIR)
        self.max_test_count = kwargs.get("count") or const.MAX_TEST_COUNT
        self.num = kwargs.get("len") or const.ARG_LENGTH
        range = kwargs["range"]
        self.min = range[0]
        self.max = range[1]
        self.num = min(self.max - self.min + 1, self.num)
        if kwargs.get("generate") is False:
            self.push_swap = (dir / const.PUSH_SWAP_NAME).resolve()
            self.checker = (dir / const.CHECKER_NAME).resolve()
            self.validate_executable(self.push_swap)
            self.validate_executable(self.checker)
            self.op_count: Counter[int] = Counter()
            self.cases: list[TesterResult] = []

    def validate_executable(self, command: Path) -> None:
        if not command.is_file():
            raise CommandNotFoundError(command)
        if not os.access(command, os.X_OK):
            raise ExecutePermissionError(command)

    def exec_commands(self) -> None:
        args = self.generate_args()
        print(
            f"Test {len(set(args))} cases: arg_length={self.num} range=({self.min}, {self.max})"
        )
        for arg in args:
            str_arg = list(map(str, list(arg)))
            self.exec_command(str_arg)

    def exec_command(self, args: list[str]) -> None:
        proc_push_swap = subprocess.run(
            [self.push_swap, *args], capture_output=True, text=True
        )
        proc_checker = subprocess.run(
            [self.checker, *args],
            input=proc_push_swap.stdout,
            capture_output=True,
            text=True,
        )
        self.process_command_result(args, proc_push_swap, proc_checker)

    def process_command_result(
        self,
        args: list[str],
        proc_push_swap: subprocess.CompletedProcess[str],
        proc_checker: subprocess.CompletedProcess[str],
    ) -> None:
        nl_count = proc_push_swap.stdout.count("\n")
        is_correct = proc_checker.stdout == "OK\n"
        case = TesterResult(args, nl_count, is_correct)
        self.cases.append(case)
        self.op_count[nl_count] += 1
        if is_correct:
            print_colored(".", const.CODE_GREEN, end="", flush=True)
        else:
            print_colored("F", const.CODE_RED, end="", flush=True)

    def show_op_count(self) -> None:
        print("\n---- Result ----")
        keys = sorted(self.op_count.elements())
        print(f"max   : {keys[-1]}")
        print(f"median: {median_high(keys)}")
        print(f"min   : {keys[0]}")
        print_colored(f"See {const.LOG_FILE_NAME} for details", const.CODE_CYAN)

    def output_result(self) -> None:
        with open(const.LOG_FILE_NAME, mode="w") as f:
            for case in self.cases:
                f.write(f"{case}\n")

    def generate_args(self) -> list[tuple[int, ...]]:
        return generate_args(self.num, self.min, self.max, self.max_test_count)
