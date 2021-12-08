from typing import List


def count_letters(outputs: List[str]) -> int:
    """Counts the number of letters in the inputs"""
    letters = 0
    admissible_lens = {2, 3, 4, 7}
    for output in outputs:
        for word in output.split(" "):
            if len(word) in admissible_lens:
                letters += 1
    return letters


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        raw_data = f.readlines()
        inputs = []
        outputs = []
        for entry in raw_data:
            input, output = entry.split(" | ")
            inputs.append(input)
            outputs.append(output.rstrip())
    return count_letters(outputs)


if __name__ == "__main__":
    result = main()
    print(result)
