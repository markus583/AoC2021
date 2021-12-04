import numpy as np


def get_winner(bingo_numbers: list, guesses: list) -> int:
    """Get the winner

    :param bingo_numbers: list of bingo numbers
    :param guesses: list of guesses from players
    :return: sum of unmarked numbers from last player to hit all * bingo number that caused a win
    """
    bingo_numbers = np.array(bingo_numbers)
    guesses = np.array(guesses).reshape((-1, 5, 5))
    del_counter = 0
    for i, _ in enumerate(bingo_numbers):
        winning_numbers = bingo_numbers[: i + 5]
        for guess_index, guess in enumerate(guesses):
            if not np.any(guess):
                continue
            for col in range(5):
                if np.all(np.isin(guess[:, col], winning_numbers)):
                    unmarked_numbers_sum = np.sum(
                        guess[~np.isin(guess, winning_numbers)]
                    )
                    if del_counter < guesses.shape[0] - 1:
                        del_counter += 1
                        guesses[guess_index] = 0
                        break
                    return unmarked_numbers_sum * bingo_numbers[i + 4]

            for row in range(5):
                if np.all(np.isin(guess[row, :], winning_numbers)):
                    unmarked_numbers_sum = np.sum(
                        guess[~np.isin(guess, winning_numbers)]
                    )
                    if del_counter < guesses.shape[0] - 1:
                        del_counter += 1
                        guesses[guess_index] = 0
                        break
                    return unmarked_numbers_sum * bingo_numbers[i + 4]


def main() -> int:
    """Main function"""
    with open("input.txt", "r", encoding="utf-8") as f:
        bingo_numbers = [int(number) for number in f.readline().split(",")]
        guesses = [f.rstrip() for f in f.readlines()[1:]]
        guesses_proc = [guess.split(" ") for guess in guesses]
        guesses_proc = [
            [int(number) if number.isnumeric() else None for number in guess]
            for guess in guesses_proc
        ]
        guesses_proc = [
            [number for number in guess if number is not None]
            for guess in guesses_proc
            if guess != [None]
        ]
        return get_winner(bingo_numbers, guesses_proc)


if __name__ == "__main__":
    result = main()
    print(result)
