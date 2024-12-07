import argparse
import logging
from math import prod
from re import findall

logger = logging.getLogger(__name__)


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="puzzle input file to be parsed", type=str)
    parser.add_argument(
        "--log", help="display log messages to console", action="store_true"
    )
    args = parser.parse_args()
    return args


def setup_log(args):
    if args.log:
        logging.basicConfig(level=logging.DEBUG)


def process_input(filename: str) -> str:
    with open(filename, "r") as input:
        puzzle_input = input.read()
    return puzzle_input


def find_muls(code: str) -> list[list]:
    matches = findall(r"mul\([\d+,]+\d+\)", code)
    numbers: list = []
    for match in matches:
        elements = [int(x) for x in match.strip("mul()").split(",")]
        numbers.append(elements)
    return numbers


def calculate_sum_of_muls(muls: list[list]) -> int:
    added_muls: int = 0
    for mul in muls:
        added_muls += prod(mul)
    return added_muls


if __name__ == "__main__":
    args = setup_args()
    setup_log(args)
    corrupted_muls: str = process_input(args.input)
    matched_muls: list[list] = find_muls(corrupted_muls)
    sum_of_muls: int = calculate_sum_of_muls(matched_muls)
    print("Answer to part one:", sum_of_muls)
