from typing import List


def pilot(directions: List[str]) -> int:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0

    for direction in directions:
        move = int(direction[-1])
        if "forward" in direction:
            horizontal += move
            depth += aim * move
        elif "up" in direction:
            aim -= move
        else:
            aim += move
    return horizontal * depth


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        directions = [f.rstrip() for f in f.readlines()]
    return pilot(directions)


if __name__ == "__main__":
    result = main()
    print(result)
