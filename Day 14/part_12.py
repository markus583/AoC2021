from collections import Counter
from typing import Dict


def count_after_insertions(
    base: str, c: Counter, rules: Dict[str, str], iterations: int
) -> int:
    for rule in c:
        if rule in base:
            c[rule] = base.count(rule)

    for i in range(iterations):
        update_counter = c.copy()
        for rule in rules:
            if c[rule] > 0:
                insertion = rules[rule]
                update_counter[rule] -= c[rule]

                update_counter[rule[0] + insertion] += c[rule]
                update_counter[insertion + rule[1]] += c[rule]

        c = update_counter

    element_counts = {v: 0 for v in rules.values()}
    for rule in c:
        element_counts[rule[0]] += c[rule] * 0.5
        element_counts[rule[1]] += c[rule] * 0.5

    return int(max(element_counts.values()) - min(element_counts.values()) + 0.5)


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        base = lines[0].strip()
        c = Counter()
        rules = dict()
        for line in lines[2:]:
            line = line.rstrip()
            pattern = line[:2]
            insertion = line[-1]
            c[pattern] = 0
            rules[pattern] = insertion
    return count_after_insertions(base=base, c=c, rules=rules, iterations=40)


if __name__ == "__main__":
    result = main()
    print(result)
