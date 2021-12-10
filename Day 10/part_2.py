from statistics import median
from typing import List


def complete_incomplete_strings(raw_data: List[str]) -> int:
    open_strings = ["(", "[", "{", "<"]
    close_strings = [")", "]", "}", ">"]
    scores = []
    for line in raw_data:
        stack = []
        is_corrupted = False
        for i, char in enumerate(line):
            if char in open_strings:
                stack.append(char)
            elif char in close_strings:
                pop_char = stack.pop()
                if open_strings.index(pop_char) == close_strings.index(char):
                    continue
                elif open_strings.index(pop_char) != close_strings.index(char):
                    is_corrupted = True
        if not is_corrupted:
            stack.reverse()  # fixing sequence is reversed from input order
            score = 0
            for char in stack:
                if char == "(":
                    score *= 5
                    score += 1
                elif char == "[":
                    score *= 5
                    score += 2
                elif char == "{":
                    score *= 5
                    score += 3
                elif char == "<":
                    score *= 5
                    score += 4
            scores.append(score)

    return median(scores)


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        raw_data = f.read().splitlines()
    return complete_incomplete_strings(raw_data)


if __name__ == "__main__":
    result = main()
    print(result)
