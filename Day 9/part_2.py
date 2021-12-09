from typing import Tuple, List, Any

import numpy as np


def find_local_minima(data: List[List[int]]) -> List[Tuple[int, int, int] | Any]:
    """Find the local minima in the data.

    :param data: The data to find the local minima in.
    :return: The sum of the data values of the local minima.
    """
    data = np.array(data)
    minima = []
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            down, left, right, up = get_neighbors(data, i, j, len(row))
            if col < up and col < down and col < left and col < right:
                minima.append(([i, j, data[i, j]]))
    return minima


def get_neighbors(data, i, j, len_row):
    up = data[i - 1][j]
    if not i >= len(data) - 1:
        down = data[i + 1][j]
    left = data[i][j - 1]
    if not j >= len_row - 1:
        right = data[i][j + 1]
    if i == 0 and j == 0:
        left = np.inf
        up = np.inf
    elif i == 0:
        up = np.inf
    elif j == 0:
        left = np.inf
    if i == len(data) - 1 and j == len_row - 1:
        right = np.inf
        down = np.inf
    elif i == len(data) - 1:
        down = np.inf
    elif j == len_row - 1:
        right = np.inf
    return down, left, right, up


def calculate_largest_basins(
    minima: List[Tuple[int, int, int]], data: List[List[int]]
) -> int:
    """Calculate the largest basins in the data.

    :param data: The data to calculate the largest basins in.
    :param minima: The minima to calculate the largest basins in.
    :return: The largest basin.
    """
    data = np.array(data)
    basins = []
    for minimum in minima:
        i = minimum[0]
        j = minimum[1]
        basin_mask = np.zeros(data.shape)
        basin_mask = move_4_directions(data, basin_mask, i, j)
        basins.append(np.sum(basin_mask))
    return np.prod(sorted(basins, reverse=True)[:3]).item()


def move_4_directions(
    data: np.ndarray, basin_mask: np.ndarray, row: int, col: int
) -> np.ndarray:

    i = row
    j = col
    basin_mask[row, col] = 1
    moving_sequence = []
    while True:
        down, left, right, up = get_neighbors(data, i, j, len(data[i]))
        if up > data[i, j] and up != 9 and up != np.inf and basin_mask[i - 1, j] == 0:
            i -= 1
            basin_mask[i, j] = 1
            moving_sequence.append("up")
        elif (
            down > data[i, j]
            and down != 9
            and down != np.inf
            and basin_mask[i + 1, j] == 0
        ):
            i += 1
            basin_mask[i, j] = 1
            moving_sequence.append("down")
        elif (
            left > data[i, j]
            and left != 9
            and left != np.inf
            and basin_mask[i, j - 1] == 0
        ):
            j -= 1
            basin_mask[i, j] = 1
            moving_sequence.append("left")
        elif (
            right > data[i, j]
            and right != 9
            and right != np.inf
            and basin_mask[i, j + 1] == 0
        ):
            j += 1
            basin_mask[i, j] = 1
            moving_sequence.append("right")
        else:
            if len(moving_sequence) == 0:
                return basin_mask
            direction = moving_sequence.pop()
            if direction == "up":
                i += 1
            elif direction == "down":
                i -= 1
            elif direction == "left":
                j += 1
            elif direction == "right":
                j -= 1


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        raw_data = [
            [int(char) for char in list(line.rstrip())] for line in f.readlines()
        ]
    minima = find_local_minima(raw_data)
    return calculate_largest_basins(minima, raw_data)


if __name__ == "__main__":
    result = main()
    print(result)
