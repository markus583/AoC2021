import numpy as np


def find_local_minima(data: list) -> int:
    """Find the local minima in the data and return the sum of their data values.

    :param data: The data to find the local minima in.
    :return: The sum of the data values of the local minima.
    """
    data = np.array(data)
    minima_sum = 0
    for i, row in enumerate(data):
        for j, col in enumerate(row):
            up = data[i - 1][j]
            if not i >= len(data) - 1:
                down = data[i + 1][j]
            left = data[i][j - 1]
            if not j >= len(row) - 1:
                right = data[i][j + 1]
            if i == 0 and j == 0:
                left = np.inf
                up = np.inf
            elif i == 0:
                up = np.inf
            elif j == 0:
                left = np.inf
            if i == len(data) - 1 and j == len(row) - 1:
                right = np.inf
                down = np.inf
            elif i == len(data) - 1:
                down = np.inf
            elif j == len(row) - 1:
                right = np.inf
            if col < up and col < down and col < left and col < right:
                minima_sum += col + 1
    return minima_sum


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        raw_data = [
            [int(char) for char in list(line.rstrip())] for line in f.readlines()
        ]
    return find_local_minima(raw_data)


if __name__ == "__main__":
    result = main()
    print(result)
