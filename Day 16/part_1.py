from typing import Tuple

bits = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def hex_to_binary(content):
    binary = ""
    for c in content:
        binary += bits[c]

    print(binary)
    return binary


version_sum = 0


def process_packet(packet: str) -> Tuple[int, int]:
    global version_sum
    current_version = packet[0:3]
    version_sum += int(current_version, 2)
    packet_type = packet[3:6]
    if packet_type == "100":  # 4
        i = 6
        number = ""
        while True:
            # print(packet[i:i+5])
            number += packet[i + 1 : i + 5]
            if packet[i] == "0":
                break
            i += 5
        return i + 5, int(number, 2)
    n_bits = 0
    numbers = []
    if packet[6] == "0":
        length = packet[7 : 6 + 16]
        while n_bits < int(length, 2):
            i, number = process_packet(packet[6 + 16 + n_bits :])
            n_bits += i
            numbers.append(number)
        n_bits = 6 + 16 + n_bits
    elif packet[6] == "1":
        length = packet[7 : 6 + 12]
        n_bits = 0
        for _ in range(0, int(length, 2)):
            i, number = process_packet(packet[6 + 12 + n_bits :])
            n_bits += i
            numbers.append(number)
        n_bits = 6 + 12 + n_bits

    # perform operations
    result = 0
    if packet_type == "000":
        for number in numbers:
            result += number
    elif packet_type == "001":
        result = 1
        for number in numbers:
            result *= number
    elif packet_type == "010":
        result = min(numbers)
    elif packet_type == "011":
        result = max(numbers)
    elif packet_type == "101":
        result = 1 if numbers[0] > numbers[1] else 0
    elif packet_type == "110":
        result = 1 if numbers[0] < numbers[1] else 0
    elif packet_type == "111":
        result = 1 if numbers[0] == numbers[1] else 0

    return n_bits, result


def main() -> Tuple[int, int]:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        contents = f.readline()[:-1]

    binary_str = hex_to_binary(contents)
    return process_packet(binary_str)


if __name__ == "__main__":
    _, num = main()
    print("Part 1 solution:", version_sum)
    print("Part 2 solution:", num)
