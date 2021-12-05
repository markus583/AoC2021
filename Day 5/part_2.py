import numpy as np


def find_vents(entries: np.ndarray) -> int:
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
        elif entry[0, 0] == entry[1, 1] and entry[0, 1] == entry[1, 0]:
            if entry[0, 0] > entry[1, 0]:
                for i in range(entry[0, 0], entry[1, 0] - 1, -1):
                    diagram[entry[1, 1] - i, i] += 1
            else:
                for i in range(entry[1, 0], entry[0, 0] - 1, -1):
                    diagram[entry[1, 1] - i, i] += 1
        elif entry[1, 0] == entry[1, 1] and entry[0, 0] == entry[0, 1]:
            if entry[0, 0] > entry[1, 0]:
                for i in range(entry[1, 0], entry[0, 0] + 1):
                    diagram[i, i] += 1
            else:
                for i in range(entry[0, 0], entry[1, 0] + 1):
                    diagram[i, i] += 1
        else:
            if entry[0, 0] > entry[1, 0]:
                lower = (entry[1, 0], entry[1, 1])
                upper = (entry[0, 0], entry[0, 1])
            elif entry[0, 0] < entry[1, 0]:
                lower = (entry[0, 0], entry[0, 1])
                upper = (entry[1, 0], entry[1, 1])
            if lower[1] < upper[1]:
                for i in range(lower[0], upper[0] + 1):
                    diagram[lower[0] + i, lower[1] + i] += 1
            else:
                offset = abs(upper[1] - lower[1])
                for i in range(offset + 1):
                    diagram[upper[0] - i, upper[1] + i] += 1

    mask = np.where(diagram > 1)
    return diagram.astype(int)  #  [mask].shape[0]


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
