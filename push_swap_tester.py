#!/usr/bin/env python3

from statistics import median_high
import math
from pathlib import Path
from argparse import ArgumentParser
import subprocess
from itertools import permutations
import random
from collections import Counter

PROJECT_DIR = ".."
PUSH_SWAP_NAME = "push_swap"
CHECKER_NAME = "checker"
LOG_FILE_NAME = "result.log"

MIN_VALUE = 1
MAX_TEST_COUNT = 200
DEFAULT_NUMBER = 5

CODE_RED = 31
CODE_GREEN = 32
CODE_CYAN = 36


class Tester:
    def __init__(self, **kwargs):
        dir = kwargs.get("dir") or PROJECT_DIR
        self.max_test_count = kwargs.get("count") or MAX_TEST_COUNT
        self.num = kwargs.get("len") or DEFAULT_NUMBER
        self.min = MIN_VALUE
        self.max = self.num
        if kwargs.get("range"):
            self.min = kwargs.get("range")[0]
            self.max = kwargs.get("range")[1]
        path = Path(dir)
        self.push_swap = path / PUSH_SWAP_NAME
        self.checker = path / CHECKER_NAME
        self.op_count = Counter()
        self.cases = []

    def exec_commands(self):
        args = self.generate_args()
        print(f"Test {len(set(args))} cases: number={self.num}")
        for arg in args:
            str_arg = list(map(str, list(arg)))
            self.exec_command(str_arg)

    def exec_command(self, arg):
        proc_push_swap = subprocess.run(
            [self.push_swap, *arg], capture_output=True, text=True
        )
        proc_checker = subprocess.run(
            [self.checker, *arg],
            input=proc_push_swap.stdout,
            capture_output=True,
            text=True,
        )
        self.process_command_result(arg, proc_push_swap, proc_checker)

    def process_command_result(self, arg, proc_push_swap, proc_checker):
        nl_count = proc_push_swap.stdout.count("\n")
        is_correct = proc_checker.stdout == "OK\n"
        self.cases.append((arg, nl_count, is_correct))
        self.op_count[nl_count] += 1
        if is_correct:
            print_colored(".", CODE_GREEN, end="", flush=True)
        else:
            print_colored("F", CODE_RED, end="", flush=True)

    def show_op_count(self):
        key_len = max([len(str(key)) for key in self.op_count.keys()])
        value_len = max([len(str(value)) for value in self.op_count.values()])
        print("\n---- Result ----")
        keys = sorted(self.op_count.elements())
        print(f"max   : {keys[-1]}")
        print(f"median: {median_high(keys)}")
        print(f"min   : {keys[0]}")
        print_colored(f"See {LOG_FILE_NAME} for details", CODE_CYAN)

    def output_result(self):
        with open(LOG_FILE_NAME, mode="w") as f:
            for case in self.cases:
                f.write(self.create_case_line(case))

    @staticmethod
    def create_case_line(case):
        arg, nl_count, is_correct = case
        text = ""
        if is_correct:
            text += "[OK]"
        else:
            text += "[KO]"
        text += f"{' '.join(arg)}: {nl_count}\n"
        return text

    def generate_args(self):
        if math.factorial(self.num) > self.max_test_count:
            return self.generate_randint(self.num)
        else:
            return self.generate_permutation(self.num)

    def generate_randint(self, num: int):
        args = set()
        while len(args) < self.max_test_count:
            arg = list(range(self.min, self.max + 1))
            random.shuffle(arg)
            args.add(tuple(arg[: self.num]))
        return args

    def generate_permutation(self, num: int):
        return list(permutations(range(self.min, self.max + 1)))


def main():
    args = parse_arguments()
    tester = Tester(**vars(args))
    if args.generate:
        tester.max_test_count = 1
        print(" ".join([str(arg) for arg in tester.generate_args().pop()]))
    else:
        tester.exec_commands()
        tester.show_op_count()
        tester.output_result()


def parse_arguments():
    parser = ArgumentParser()
    parser.add_argument(
        "-l",
        dest="len",
        type=int,
        default=DEFAULT_NUMBER,
        help=f"argument length (default: {DEFAULT_NUMBER})",
    )
    parser.add_argument(
        "-c",
        dest="count",
        type=int,
        default=MAX_TEST_COUNT,
        help=f"max test count (default: {MAX_TEST_COUNT})",
    )
    parser.add_argument(
        "-d",
        dest="dir",
        type=str,
        default=PROJECT_DIR,
        help=f'project directory (default: "{PROJECT_DIR}")',
    )
    parser.add_argument(
        "-g",
        "--gen",
        dest="generate",
        action="store_true",
        help="generate random numbers (-c is ignored)",
    )
    parser.add_argument(
        "-r",
        dest="range",
        nargs=2,
        type=int,
        help=f"range of numbers (default: {MIN_VALUE}, LEN)",
        metavar=("BEGIN", "END"),
    )
    args = parser.parse_args()
    return args


def print_colored(text: str, code: int, **kwargs):
    print(f"\033[{code}m{text}\033[0m", **kwargs)


if __name__ == "__main__":
    main()
