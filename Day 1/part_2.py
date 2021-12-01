"""Day 1, part 2: Count how many list entries over sliding window of size 3 have increased compared to the previous
window """


def count_increase(measurements: list) -> int:
    """Count how many sliding windows entries have increased compared to the slding window before

    :param measurements: entries in list
    :return: count of entries that have increased
    """
    count = 0
    for i, _ in enumerate(measurements):
        if i in (0, 1):
            continue
        if i == 2:
            last_sum = measurements[i-2] + measurements[i-1] + measurements[i]
        current_sum = measurements[i] + measurements[i - 1] + measurements[i - 2]
        if current_sum > last_sum:
            count += 1
        last_sum = current_sum
    return count


def main() -> int:
    """Main function"""
    with open("input_2.txt", "r", encoding="utf-8") as f:
        entries = [int(f.rstrip()) for f in f.readlines()]
    return count_increase(entries)


if __name__ == "__main__":
    result = main()
    print(result)
