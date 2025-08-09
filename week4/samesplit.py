from collections import Counter


def count_splits(numbers):
    total = set(numbers)
    left_seen = set()

    # build the right side
    counter = Counter(numbers)
    right_seen = set(counter.keys())

    cnt = 0
    for i in range(len(numbers) - 1):
        left_seen.add(numbers[i])
        counter[numbers[i]] -= 1
        if counter[numbers[i]] == 0:
            right_seen.remove(numbers[i])

        if left_seen == right_seen == total:
            cnt += 1

    return cnt


if __name__ == "__main__":
    print(count_splits([1, 1, 1, 1]))  # 3
    print(count_splits([1, 1, 2, 1]))  # 0
    print(count_splits([1, 2, 1, 2]))  # 1
    print(count_splits([1, 2, 3, 4]))  # 0
    print(count_splits([1, 2, 1, 2, 1, 2]))  # 3

    numbers = [1, 2] * 10**5
    print(count_splits(numbers))  # 199997
    numbers = list(range(1, 10**5 + 1)) * 2
    print(count_splits(numbers))  # 1
