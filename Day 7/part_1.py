from typing import List, Tuple

import numpy as np


def calculate_alignment_coordinate(data: List[int]) -> Tuple[int, int]:
    """Calculate the alignment coordinate

    :param data: list of starting coordinates
    :return: tuple containing the best alignment coordinate and its value
    """
    data = np.array(data)
    lowest_value = data.min()
    highest_value = data.max()
    best_difference = np.inf
    best_coordinate = None
    for i in range(lowest_value, highest_value + 1):
        current_difference = 0
        for value in data:
            current_difference += abs(value - i)
        if current_difference < best_difference:
            best_difference = current_difference
            best_coordinate = i
    return best_coordinate, best_difference


def main() -> Tuple[int, int]:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        raw_data = [int(n) for n in f.readline().split(",")]
    return calculate_alignment_coordinate(raw_data)


if __name__ == "__main__":
    result = main()
    print(result)
