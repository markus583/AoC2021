from typing import List


def get_adjacents(data: List[List[str]]):
    adjacents = dict()
    for i, row in enumerate(data):
        if row[0] not in adjacents.keys():
            adjacents[row[0]] = set()
        adjacents[row[0]].add((row[1]))
        if row[1] not in adjacents.keys():
            adjacents[row[1]] = set()
        adjacents[row[1]].add((row[0]))
    return adjacents


def is_lower_in_list(data: List[str], node) -> bool:
    for i in data:
        if i.islower() and i != "start" and i != "end" and i != node:
            return True
    return False


def solve_dfs(data: List[List[str]]) -> int:
    """Your goal is to find the number of distinct paths that start at start, end at end,
    and don't visit small caves more than once.
    There are two types of caves: big caves (written in uppercase, like A) and small caves (written in lowercase, like b).
    It would be a waste of time to visit any small cave more than once,
    but big caves are large enough that it might be worth visiting them multiple times.
    So, all paths you find should visit small caves at most once, and can visit big caves any number of times."""
    adjacents = get_adjacents(data)
    print(adjacents)
    fringe = []
    current = "start"
    fringe.append([current])
    n_paths = 0
    paths = []
    current_path = []
    try:
        while len(fringe) > 0:
            current = fringe[-1].pop()
            current_path.append(current)
            while (
                any(
                    current_path.count(element) > 1
                    for element in current_path
                    if element.islower()
                )
                and len(current_path) > 1
            ):
                current_path.pop()
                while len(fringe[-1]) == 0:
                    if len(fringe) == 1:
                        if not fringe[0]:
                            return n_paths
                    current_path.pop()
                    fringe.pop()
                current = fringe[-1].pop()
                current_path.append(current)
            if current == "end":
                n_paths += 1
                if current_path not in paths:
                    paths.append(current_path.copy())
                current_path.pop()
            else:
                nodes = []
                for node in sorted(adjacents[current]):
                    if node != "start":
                        nodes.append(node)
                fringe.append(nodes)
    except IndexError:
        pass
    return n_paths


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        raw_data = [line.rstrip().split("-") for line in f.readlines()]
    return solve_dfs(raw_data)


if __name__ == "__main__":
    result = main()
    print(result)
