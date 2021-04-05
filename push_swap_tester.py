#!/usr/bin/env python3

import sys

from src import const
from src.exception import PushSwapError
from src.parse import parse_arguments
from src.print import print_colored
from src.tester import Tester


def main() -> None:
    args = parse_arguments(sys.argv[1:])
    try:
        tester = Tester(**vars(args))
        if args.generate:
            tester.max_test_count = 1
            print(" ".join([str(arg) for arg in tester.generate_args().pop()]))
        else:
            tester.exec_commands()
            tester.show_op_count()
            tester.output_result()
    except PushSwapError as e:
        print_colored(f"Error: {e}", const.CODE_RED)


if __name__ == "__main__":
    main()
