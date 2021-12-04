import numpy as np
from scipy.stats import mode


def calc_mode_column(bit_list: list) -> int:
    bit_list_array = np.array([list(bit) for bit in bit_list], dtype=int)
    column_modes = mode(bit_list_array, axis=0).mode
    column_modes_inverted = np.invert(column_modes.astype(bool)).astype(int)
    bin_str_gamma = "".join([str(elem) for elem in column_modes.tolist()[0]])
    bin_str_eps = "".join([str(elem) for elem in column_modes_inverted.tolist()[0]])
    gamma_rate: int = int(bin_str_gamma, 2)
    epsilon_rate: int = int(bin_str_eps, 2)
    return gamma_rate * epsilon_rate


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        bit_list = [f.rstrip() for f in f.readlines()]
    return calc_mode_column(bit_list)


if __name__ == "__main__":
    result = main()
    print(result)
