from itertools import pairwise


def process_input(filename: str) -> list[list[int]]:
    with open(filename, "r") as puzzle_input:
        cases: list[list[int]] = []
        for line in puzzle_input:
            report = [int(x.strip()) for x in line.split(" ")]
            cases.append(report)
    return cases


def is_safe(report: list):
    checklist: list[bool] = []
    pairs = list(pairwise(report))
    for pair in pairs:
        if (pair[0] > pair[1]) and (abs(pair[0] - pair[1]) <= 3):
            checklist.append(True)
        elif (pair[0] < pair[1]) and (abs(pair[0] - pair[1]) <= 3):
            checklist.append(False)
    if sum(checklist) == len(pairs) or (
        len(checklist) == len(pairs) and sum(checklist) == 0
    ):
        return True


if __name__ == "__main__":
    test_cases = process_input("puzzle_input")
    number_of_safe: int = 0
    for case in test_cases:
        if is_safe(case):
            number_of_safe += 1
    print("Answer to part one:", number_of_safe)
