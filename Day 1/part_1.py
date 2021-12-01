"""Day 1, part 1: Count how many list entries have increased compared to the previous entry"""


def count_increase(measurements: list) -> int:
    """Count how many list entries have increased compared to the previous entry

    :param measurements: entries in list
    :return: count of entries that have increased
    """
    count = 0
    for i, entry in enumerate(measurements):
        if i == 0:
            continue
        if entry > measurements[i - 1]:
            count += 1
    return count


def main() -> int:
    """Main function"""
    with open("input_1.txt", "r", encoding="utf-8") as f:
        entries = [int(f.rstrip()) for f in f.readlines()]
    return count_increase(entries)


if __name__ == "__main__":
    result = main()
    print(result)
