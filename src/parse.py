from __future__ import annotations

from argparse import ArgumentParser, Namespace, RawTextHelpFormatter
from pathlib import Path
from typing import List

from src import const


def parse_arguments(args: List[str]) -> Namespace:
    parser = init_praser()
    ret = parser.parse_args(args)
    validate_arguments(parser, ret)
    return ret


def init_praser() -> ArgumentParser:
    parser = ArgumentParser(formatter_class=PushSwapTesterHelpFormatter)
    parser.add_argument(
        "-l",
        "--len",
        dest="len",
        type=positive_int,
        default=const.ARG_LENGTH,
        help=f"argument length   (default: {const.ARG_LENGTH})",
        metavar="number",
    )
    parser.add_argument(
        "-c",
        "--count",
        dest="count",
        type=positive_int,
        default=const.MAX_TEST_COUNT,
        help=f"max test count    (default: {const.MAX_TEST_COUNT})",
        metavar="number",
    )
    parser.add_argument(
        "-d",
        "--dir",
        dest="dir",
        type=Path,
        default=const.PROJECT_DIR,
        help=f'project directory (default: "{const.PROJECT_DIR}")',
        metavar="path",
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
        "--range",
        dest="range",
        nargs=2,
        type=int,
        default=(const.INT_MIN, const.INT_MAX),
        help=f"range of numbers  (default: {const.INT_MIN}, {const.INT_MAX})",
        metavar=("min", "max"),
    )
    return parser


def positive_int(string: str) -> int:
    num = int(string)
    if num < 0:
        raise ValueError(num)
    return num


def validate_arguments(parser: ArgumentParser, ret: Namespace) -> None:
    validate_range(parser, ret)
    validate_dir(parser, ret)


def validate_range(parser: ArgumentParser, ret: Namespace) -> None:
    if ret.range[0] > ret.range[1]:
        parser.error(f"argument -r: invalid range: '{ret.range[0]}' '{ret.range[1]}'")


def validate_dir(parser: ArgumentParser, ret: Namespace) -> None:
    if not ret.dir.is_dir():
        parser.error(f"argument -d: is not a directory: '{ret.dir}'")


class PushSwapTesterHelpFormatter(RawTextHelpFormatter):
    def __init__(
        self,
        prog: str,
        indent_increment: int = 2,
        max_help_position: int = 32,
        width: int | None = None,
    ) -> None:
        super().__init__(
            prog,
            indent_increment=indent_increment,
            max_help_position=max_help_position,
            width=width,
        )
