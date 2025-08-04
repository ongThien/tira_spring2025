def count_rounds(numbers: list[int]) -> int:
    # Instead of simulating the process directly
    # we can preprocess the positions of each number
    # and count how many discontinuities there are in the positions.
    n = len(numbers)
    pos = [0] * (n + 1)
    for i, num in enumerate(numbers):
        pos[num] = i

    rounds = 1
    for i in range(2, n + 1):
        # we start from 2 because there is no 0 in numbers
        # and we're checking i vs i - 1
        # i.e. if index of 2 is less than index of 1, then we need another round
        if pos[i] < pos[i - 1]:
            rounds += 1

    return rounds


if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4]))  # 1
    print(count_rounds([1, 3, 2, 4]))  # 2
    print(count_rounds([4, 3, 2, 1]))  # 4
    print(count_rounds([1]))  # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8]))  # 4

    n = 10**5
    numbers = list(reversed(range(1, n + 1)))
    print(count_rounds(numbers))  # 100000
