from typing import List

import numpy as np


def fold_along_coordinates(splits: List[List[int]], folds: List[List[int]]) -> int:
    """Fold along coordinates in folds

    :param splits: List of initial coordinates
    :param folds: List of folds to be done
    :return: Number of coordinates after folding
    """
    # initial matrix size (depends on the largest coordinate)
    if folds[0][0] == "x":
        y_max = folds[0][1] * 2
        x_max = folds[1][1] * 2
    else:
        y_max = folds[1][1] * 2
        x_max = folds[0][1] * 2

    fill_matrix = np.zeros(shape=(x_max + 1, y_max + 1))
    # fill the matrix with the initial coordinates
    for split in splits:
        fill_matrix[split[1], split[0]] = 1

    for fold in folds:
        if fold[0] == "x":
            fill_matrix = fill_matrix[:, : fold[1]]
            for split in splits:
                if split[0] <= fill_matrix.shape[1]:  # if the split is in the matrix
                    continue
                # if the split is not in the matrix
                x_offset = (
                    split[0] - (split[0] - fill_matrix.shape[1]) * 2
                )  # new x coordinate
                split[0] = x_offset
                fill_matrix[split[1], x_offset] = 1

        elif fold[0] == "y":
            fill_matrix = fill_matrix[: fold[1], :]
            for split in splits:
                if split[1] <= fill_matrix.shape[0]:  # if the split is in the matrix
                    continue
                # if the split is not in the matrix
                y_offset = (
                    split[1] - (split[1] - fill_matrix.shape[0]) * 2
                )  # new y coordinate
                split[1] = y_offset
                fill_matrix[y_offset, split[0]] = 1

    print(fill_matrix)  # JPZCUAUR
    return np.sum(fill_matrix).item()


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    coordinates = [
        line.rstrip() for line in lines if not (line.startswith("f") or len(line) == 1)
    ]
    folds = [
        [int(c) if len(c) <= 3 else c[-1] for c in line.rstrip().split("=")]
        for line in lines
        if line.startswith("f")
    ]
    splits = [[int(n) for n in coord.split(",")] for coord in coordinates]
    return fold_along_coordinates(splits, folds)


if __name__ == "__main__":
    result = main()
    print(result)
