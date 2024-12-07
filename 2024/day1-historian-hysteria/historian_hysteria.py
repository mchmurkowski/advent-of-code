def process_input(filename: str) -> tuple[list, list]:
    with open(filename, "r") as puzzle_input:
        left: list = []
        right: list = []
        for line in puzzle_input:
            left_item, right_item = line.split("   ")
            left.append(int(left_item))
            right.append(int(right_item.strip()))
        return left, right


def calculate_distance(left: list[int], right: list[int]) -> int:
    left.sort()
    right.sort()
    zipped: list[tuple[int, int]] = list(zip(left, right))
    total_distance: int = 0
    for id_pair in zipped:
        id1, id2 = id_pair
        distance = abs(id1 - id2)
        total_distance += distance
    return total_distance


def calculate_similarity_score(left: list, right: list):
    similarity_score: int = 0
    for item in left:
        similarity_score += item * right.count(item)
    return similarity_score


if __name__ == "__main__":
    left, right = process_input("puzzle_input")
    print("Answer to part one (distance):", calculate_distance(left, right))
    print(
        "Answer to part two (similarity score):",
        calculate_similarity_score(left, right),
    )
