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
        else:
            pass
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
