import numpy as np
from scipy.stats import mode


def rating(candidates: np.ndarray, invert: bool = False) -> int:
    """Helper function returning the rating of the candidates.

    :param candidates: binary array of candidates
    :param invert: whether to use maximal or minimal rating
    :return: candidate rating in the form of a number
    """
    iterations = candidates.shape[1]
    for i in range(iterations):
        column_mode = mode(candidates, axis=0).mode[0, i]
        if invert:
            column_mode = np.invert(column_mode.astype(bool)).astype(int)
        if np.unique(np.unique(candidates[:, i], return_counts=True)[1]).shape[0] == 1:
            if invert:
                column_mode = 0
            else:
                column_mode = 1
            mask = candidates[:, i] == column_mode
            candidates = candidates[mask]
        mask = candidates[:, i] == column_mode
        candidates = candidates[mask]
        if candidates.shape[0] == 1:
            return int("".join([str(elem) for elem in candidates.tolist()[0]]), 2)
    raise ValueError("Could not find a single candidate")


def life_support_rating(bit_list: list) -> int:
    """Function to calculate the rating of the life support system.

    :param bit_list: list of binary strings from input file
    :return: rating of the life support system
    """
    bit_list_array = np.array([list(bit) for bit in bit_list], dtype=int)
    oxygen_rating = rating(bit_list_array, invert=False)
    co2_rating = rating(bit_list_array, invert=True)
    return oxygen_rating * co2_rating


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        bit_list = [f.rstrip() for f in f.readlines()]
    return life_support_rating(bit_list)


if __name__ == "__main__":
    result = main()
    print(result)
