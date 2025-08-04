def find_rounds(numbers: list[int]) -> list[list[int]]:
    rounds = []
    cur = 1
    while cur <= len(numbers):
        cur_round = []
        for n in numbers:
            if n == cur:
                cur_round.append(cur)
                cur += 1

        rounds.append(cur_round)

    return rounds


if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]

    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]
