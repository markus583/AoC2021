from typing import List


def correct_signal(inputs: List[str], outputs: List[str]) -> int:
    final_output = 0
    for possible_input, possible_output in zip(inputs, outputs):
        keys = dict()
        line = sorted(possible_input.split(" "), key=len, reverse=False)

        # first, tackle easy cases
        for seq in line:
            if len(seq) == 2:
                keys["c"] = {seq[0], seq[1]}
                keys["f"] = {seq[0], seq[1]}
            elif len(seq) == 3:
                all_keys_7 = {seq[0], seq[1], seq[2]}
                keys["a"] = all_keys_7.symmetric_difference(keys["c"])
            elif len(seq) == 4:
                all_keys_4 = {seq[0], seq[1], seq[2], seq[3]}
                keys["b"] = all_keys_4.symmetric_difference(keys["c"])
                keys["d"] = all_keys_4.symmetric_difference(keys["c"])
            elif len(seq) == 7:
                all_keys = {s for s in seq}
                keys["e"] = all_keys.symmetric_difference(all_keys_4.union(all_keys_7))
                keys["g"] = all_keys.symmetric_difference(all_keys_4.union(all_keys_7))

        # some helper variables - needed to ensure each case is visited only once
        exhausted_e = False
        exhausted_d = False
        exhausted_c = False

        # now, tackle the rest
        for seq in line:
            all_keys = {s for s in seq}
            if len(seq) == 6:
                if len(keys["d"].intersection(all_keys)) == 1 and not exhausted_d:
                    overlap_key = keys["d"].intersection(all_keys)
                    keys["d"] = keys["d"].symmetric_difference(overlap_key)
                    keys["b"] = keys["b"].intersection(overlap_key)
                    exhausted_d = True
                if len(keys["c"].intersection(all_keys)) == 1 and not exhausted_c:
                    overlap_key = keys["c"].intersection(all_keys)
                    keys["c"] = keys["c"].symmetric_difference(overlap_key)
                    keys["f"] = keys["f"].intersection(overlap_key)
                    exhausted_c = True
                if len(keys["e"].intersection(all_keys)) == 1 and not exhausted_e:
                    overlap_key = keys["e"].intersection(all_keys)
                    keys["e"] = keys["e"].symmetric_difference(overlap_key)
                    keys["g"] = keys["g"].intersection(overlap_key)
                    exhausted_e = True

        mappings = {
            0: list(keys["a"])[0]
            + list(keys["b"])[0]
            + list(keys["c"])[0]
            + list(keys["e"])[0]
            + list(keys["f"])[0]
            + list(keys["g"])[0],
            1: list(keys["c"])[0] + list(keys["f"])[0],
            2: list(keys["a"])[0]
            + list(keys["c"])[0]
            + list(keys["d"])[0]
            + list(keys["e"])[0]
            + list(keys["g"])[0],
            3: list(keys["a"])[0]
            + list(keys["c"])[0]
            + list(keys["d"])[0]
            + list(keys["f"])[0]
            + list(keys["g"])[0],
            4: list(keys["b"])[0]
            + list(keys["c"])[0]
            + list(keys["d"])[0]
            + list(keys["f"])[0],
            5: list(keys["a"])[0]
            + list(keys["b"])[0]
            + list(keys["d"])[0]
            + list(keys["f"])[0]
            + list(keys["g"])[0],
            6: list(keys["a"])[0]
            + list(keys["b"])[0]
            + list(keys["d"])[0]
            + list(keys["e"])[0]
            + list(keys["f"])[0]
            + list(keys["g"])[0],
            7: list(keys["c"])[0] + list(keys["f"])[0] + list(keys["a"])[0],
            8: list(keys["a"])[0]
            + list(keys["b"])[0]
            + list(keys["d"])[0]
            + list(keys["e"])[0]
            + list(keys["f"])[0]
            + list(keys["g"])[0]
            + list(keys["c"])[0],
            9: list(keys["a"])[0]
            + list(keys["b"])[0]
            + list(keys["d"])[0]
            + list(keys["f"])[0]
            + list(keys["g"])[0]
            + list(keys["c"])[0],
        }

        output_string = ""
        output_splitted = possible_output.split(" ")
        for i, out in enumerate(output_splitted):
            out_set = {s for s in out}
            for key, item in zip(mappings.keys(), mappings.values()):
                mapping_set = {s for s in item}
                if out_set == mapping_set:
                    output_string += str(key)
        final_output += int(output_string)
    return final_output


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        raw_data = f.readlines()
    inputs = []
    outputs = []
    for entry in raw_data:
        segments, output = entry.split(" | ")
        inputs.append(segments)
        outputs.append(output.rstrip())
    return correct_signal(inputs, outputs)


if __name__ == "__main__":
    result = main()
    print(result)
