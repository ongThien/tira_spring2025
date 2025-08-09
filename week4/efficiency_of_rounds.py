import random
import time


def count_rounds_exercise_week2(numbers: list[int]) -> int:
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


def count_rounds_example_week4(numbers: list[int]) -> int:
    n = len(numbers)

    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i

    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1

    return rounds


n = 10**7
data = list(range(1, n + 1))
random.shuffle(data)

start = time.time()
count_rounds_exercise_week2(data)
end = time.time()
print("Running time when using a list:", round(end - start, 2), "s")

start = time.time()
count_rounds_example_week4(data)
end = time.time()
print("Running time when using a dictionary:", round(end - start, 2), "s")

# Discussion:
# Even though both list and dict are O(1) lookup,
# the list has lower constant-time cost and much better memory access patterns.
# Dictionaries have more overhead like hashing keys, collision handling and are not contiguous in memory.
