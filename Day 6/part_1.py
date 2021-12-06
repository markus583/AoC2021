from typing import List

import numpy as np


def count_after(data: List[int], iteration: int) -> int:
    data = np.array(data)
    for i in range(iteration):
        print(iteration, data.shape[0])
        for j, flower in enumerate(data):
            if flower == 0:
                data[j] = 6
                data = np.append(data, 8)
            else:
                data[j] = data[j] - 1
    return data


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        raw_data = [int(n) for n in f.readline().split(",")]
    return count_after(raw_data, 256).shape


if __name__ == "__main__":
    result = main()
    print(result)
