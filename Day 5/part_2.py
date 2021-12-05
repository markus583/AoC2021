import numpy as np


def find_vents(entries: np.ndarray) -> int:
    """Find the number of vents

    :param entries: The entries of the map
    :return: The number of vents
    """
    diagram = np.zeros(shape=(np.max(entries) + 1, np.max(entries) + 1))
    for entry in entries:
        if entry[0, 0] == entry[1, 0]:
            if entry[1, 1] < entry[0, 1]:
                diagram[entry[1, 1] : entry[0, 1] + 1, entry[0, 0]] += 1
            else:
                diagram[entry[0, 1] : entry[1, 1] + 1, entry[0, 0]] += 1
        elif entry[0, 1] == entry[1, 1]:
            if entry[0, 0] > entry[1, 0]:
                diagram[entry[1, 1], entry[1, 0] : entry[0, 0] + 1] += 1
            else:
                diagram[entry[1, 1], entry[0, 0] : entry[1, 0] + 1] += 1
        else:
            if entry[0, 0] > entry[1, 0]:
                lower = (entry[1, 0], entry[1, 1])
                upper = (entry[0, 0], entry[0, 1])
            else:
                lower = (entry[0, 0], entry[0, 1])
                upper = (entry[1, 0], entry[1, 1])
            offset = (upper[0] - lower[0], upper[1] - lower[1])
            if (offset[0] > 0) and offset[1] < 0:
                for i in range(offset[0] + 1):
                    diagram[upper[1] + i, upper[0] - i] += 1
            elif (offset[0] > 0) and offset[1] > 0:
                for i in range(offset[0] + 1):
                    diagram[lower[1] + i, lower[0] + i] += 1

    mask = np.where(diagram > 1)
    return diagram[mask].shape[0]


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        raw_data = [f.rstrip() for f in f.readlines()]
        entries = []
        for point in raw_data:
            coords_str = point.split(" -> ")
            coords = [coords_str[0].split(","), coords_str[1].split(",")]
            entries.append(coords)

    entries = np.array(entries, dtype=int)
    return find_vents(entries)


if __name__ == "__main__":
    result = main()
    print(result)
