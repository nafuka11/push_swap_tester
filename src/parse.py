from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import List

from src import const


def parse_arguments(args: List[str]) -> Namespace:
    parser = init_praser()
    ret = parser.parse_args(args)
    if ret.range and ret.range[0] > ret.range[1]:
        parser.error(f"argument -r: invalid range: '{ret.range[0]}' '{ret.range[1]}'")
    if not ret.dir.is_dir():
        parser.error(f"argument -d: is not a directory: '{ret.dir}'")
    return ret


def init_praser() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument(
        "-l",
        dest="len",
        type=positive_int,
        default=const.ARG_LENGTH,
        help=f"argument length (default: {const.ARG_LENGTH})",
    )
    parser.add_argument(
        "-c",
        dest="count",
        type=positive_int,
        default=const.MAX_TEST_COUNT,
        help=f"max test count (default: {const.MAX_TEST_COUNT})",
    )
    parser.add_argument(
        "-d",
        dest="dir",
        type=Path,
        default=const.PROJECT_DIR,
        help=f'project directory (default: "{const.PROJECT_DIR}")',
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
        help=f"range of numbers (default: {const.MIN_VALUE}, LEN)",
        metavar=("BEGIN", "END"),
    )
    return parser


def positive_int(string: str) -> int:
    num = int(string)
    if num < 0:
        raise ValueError(num)
    return num
