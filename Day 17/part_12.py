import math
import re

def inside_target(x: int, y: int, x_min: int, x_max: int, y_min: int, y_max: int) -> bool:
    """Check if a point is inside the target

    :param x: current x coordinate
    :param y: current y coordinate
    :param x_min: left boundary of the target
    :param x_max: right boundary of the target
    :param y_min: lower boundary of the target
    :param y_max: upper boundary of the target
    :return: whether the point is inside the target
    """
    return x_min <= x <= x_max and y_min <= y <= y_max

def fire(dx: int, dy: int, x_min: int, x_max: int, y_min: int, y_max: int) -> float:
    """Calculate the maximum height reached given a slope

    :param dx: x-axis slope
    :param dy: y-axis slope
    :param x_min: left boundary of the target
    :param x_max: right boundary of the target
    :param y_min: lower boundary of the target
    :param y_max: upper boundary of the target
    :return: Maximum height reached, or -inf if the slope is not valid, i.e. target is not reachable
    """
    x, y, max_height = 0, 0, 0
    while y >= y_min:  # as long as we are not beyond target
        x, y = x + dx, y + dy
        max_height = max(max_height, y)
        # add drag
        if dx > 0:
            dx -= 1
        elif dx < 0:
            dx += 1
        dy -= 1
        if inside_target(x, y, x_min, x_max, y_min, y_max):
            return max_height
    return -math.inf

def solve(x_min: int, x_max: int, y_min: int, y_max: int) -> (int, int):
    trials = {
        (dx, dy): height
        for dx in range(0, x_max + 1)  # loop over all possible slopes
        for dy in range(y_min, -y_min)  # all needed!
        # finally, use Walrus operator!
        if (height := fire(dx, dy, x_min, x_max, y_min, y_max)) > -math.inf
    }
    return max(trials.values()), len(trials)



def main() -> (int, int):
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        contents = f.readline()
    x_min, x_max, y_min, y_max = map(
        int, re.search(
            r"(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", contents
        ).groups()
    )
    return solve(x_min, x_max, y_min, y_max)


if __name__ == "__main__":
    max_height, eligible_trials = main()
    print(f"Result part 1: {max_height}")
    print(f"Result part 2: {eligible_trials}")
