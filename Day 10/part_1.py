from typing import List


def find_corrupted_strings(raw_data: List[str]) -> int:
    open_strings = ["(", "[", "{", "<"]
    close_strings = [")", "]", "}", ">"]
    syntax_error_score = 0
    for line in raw_data:
        stack = []
        for char in line:
            if char in open_strings:
                stack.append(char)
            elif char in close_strings:
                if len(stack) == 0:
                    break
                if open_strings.index(stack.pop()) != close_strings.index(char):
                    if char == ">":
                        syntax_error_score += 25137
                    elif char == "}":
                        syntax_error_score += 1197
                    elif char == "]":
                        syntax_error_score += 57
                    elif char == ")":
                        syntax_error_score += 3
                    continue
    return syntax_error_score


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        raw_data = f.read().splitlines()
    return find_corrupted_strings(raw_data)


if __name__ == "__main__":
    result = main()
    print(result)
