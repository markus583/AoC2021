from collections import Counter
from typing import List

import numpy as np


def count_after(data: List[int], iteration: int) -> int:
    """Perform n iteration of exponential growth given data.

    :param data: list of integers in [0, 5]
    :param iteration: number of iterations
    :return: number of elements after iterations
    """
    data = np.array(data)
    count = Counter(data)
    for key in range(9):
        if key not in count.keys():
            count[key] = 0
    for _ in range(iteration):
        n_new_6 = count[0]
        for key in sorted(count.keys()):
            if not key == 0:
                count[key - 1] = count[key]
            else:
                n_new_8 = count[0]
        count[8] = n_new_8
        count[6] += n_new_6

    return count.total()


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        raw_data = [int(n) for n in f.readline().split(",")]
    return count_after(raw_data, 256)


if __name__ == "__main__":
    result = main()
    print(result)
