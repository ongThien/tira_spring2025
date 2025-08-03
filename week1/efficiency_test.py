import random
import time


def count_even1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result


def count_even2(numbers):
    return sum(x % 2 == 0 for x in numbers)


# Compare the efficiencies of the two implementations using a list that contains 10^7 randomly chosen numbers.
numbers = [random.randint(1, 10**6) for _ in range(10**7)]

start = time.time()
res = count_even1(numbers)
end = time.time()
print("Implementation 1 run time:", round(end - start, 2), "s")

start = time.time()
res2 = count_even2(numbers)
end = time.time()
print("Implementation 2 run time:", round(end - start, 2), "s")
