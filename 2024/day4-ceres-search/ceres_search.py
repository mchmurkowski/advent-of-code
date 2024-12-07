# NOTE: this code is work in progress and is not working properly
import argparse
import re


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="puzzle input file to be parsed", type=str)
    parser.add_argument(
        "--log", help="display log messages to console", action="store_true"
    )
    args = parser.parse_args()
    return args


def process_input(filename: str) -> str:
    with open(filename, "r") as input:
        puzzle_input = input.read()
    return puzzle_input


def make_lines(word_puzzle) -> list[str]:
    # rows
    puzzle_array: list[str] = word_puzzle.split("\n")
    puzzle_array.pop(-1)
    search_lines: list[str] = puzzle_array
    # columns
    for col in range(len(puzzle_array[0])):
        col_contents: str = ""
        for row in puzzle_array:
            print(col, row, len(row), row[col])
            col_contents += row[col]
        search_lines.append(col_contents)

    # diagonals
    def walk_diagonals(array):
        array_height = len(array)
        array_width = len(array[0])
        for line in range(1, (array_height + array_width)):
            start_col = max(0, line - array_height)
            count = min(line, (array_width - start_col), array_height)
            diagonal_contents: str = ""
            for diagonal in range(0, count):
                diagonal_contents += array[min(array_height, line) - diagonal - 1][
                    start_col + diagonal
                ]
            search_lines.append(diagonal_contents)

    walk_diagonals(puzzle_array)
    # reversed diagonals
    reversed_word_puzzle: str = word_puzzle[::-1]
    reversed_puzzle_array = reversed_word_puzzle.split("\n")
    reversed_puzzle_array.pop(0)
    walk_diagonals(reversed_puzzle_array)
    return search_lines


if __name__ == "__main__":
    args = setup_args()
    word_puzzle = process_input(args.input)
    search_lines = make_lines(word_puzzle)
    xmas_hits: int = 0
    for line in search_lines:
        hits = re.findall(r"XMAS|SAMX", line)
        xmas_hits += len(hits)
    print("Answer to part one:", xmas_hits)
