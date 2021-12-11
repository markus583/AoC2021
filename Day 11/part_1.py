from typing import List

import numpy as np
import numpy.typing as npt


def get_neighbors_greater_9(
    data: npt.NDArray, flash_mask: npt.NDArray[bool]
) -> npt.NDArray:
    greater_neighbors = np.zeros(data.shape)
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            up = data[i - 1][j]
            if not i >= len(data) - 1:
                down = data[i + 1][j]
            left = data[i][j - 1]
            if not j >= len(row) - 1:
                right = data[i][j + 1]
            if i == 0 and j == 0:
                left = 0
                up = 0
            elif i == 0:
                up = 0
            elif j == 0:
                left = 0
            if i == len(data) - 1 and j == len(row) - 1:
                right = 0
                down = 0
            elif i == len(data) - 1:
                down = 0
            elif j == len(row) - 1:
                right = 0

            # diagonals
            up_left = 0
            up_right = 0
            down_left = 0
            down_right = 0
            if not i == 0 and not j == 0:
                up_left = data[i - 1][j - 1]
            if not i == 0 and not j == len(row) - 1:
                up_right = data[i - 1][j + 1]
            if not i == len(data) - 1 and not j == 0:
                down_left = data[i + 1][j - 1]
            if not i == len(data) - 1 and not j == len(row) - 1:
                down_right = data[i + 1][j + 1]

            if not i == 0:
                if flash_mask[i - 1][j]:
                    up = 0

            if not i == len(data) - 1:
                if flash_mask[i + 1][j]:
                    down = 0
            if not j == 0:
                if flash_mask[i][j - 1]:
                    left = 0
            if not j == 0 and not i == 0:
                if flash_mask[i - 1][j - 1]:
                    up_left = 0
            if not j == len(row) - 1:
                if flash_mask[i][j + 1]:
                    right = 0
            if not i == len(data) - 1 and not j == len(row) - 1:
                if flash_mask[i + 1][j + 1]:
                    down_right = 0
            if not i == 0 and not j == len(row) - 1:
                if flash_mask[i - 1][j + 1]:
                    up_right = 0
            if not i == len(data) - 1 and not j == 0:
                if flash_mask[i + 1][j - 1]:
                    down_left = 0

            neighbors = np.array(
                (up, down, left, right, up_left, up_right, down_left, down_right)
            )
            greater_neighbors[i, j] = np.sum(neighbors > 9)
    return greater_neighbors


def increase_octupus_energy_level(
    raw_data: List[List[int]], iterations: int = 100
) -> int:
    data = np.array(raw_data)
    flashes = 0
    for _ in range(1, iterations + 1):
        data += 1
        flash_mask = np.zeros(data.shape).astype(bool)
        while True:
            neighbors = get_neighbors_greater_9(data, flash_mask).astype(int)
            neighbors = np.where(~flash_mask, neighbors, 0)
            last_flash_mask = flash_mask.copy()
            flash_mask += data > 9
            data += neighbors
            if (last_flash_mask == flash_mask).all():
                data[flash_mask] = 0
                break

        flashes += np.sum(flash_mask)
    return flashes


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        raw_data = [
            [int(char) for char in list(line.rstrip())] for line in f.readlines()
        ]
    return increase_octupus_energy_level(raw_data, iterations=100)


if __name__ == "__main__":
    result = main()
    print(result)
