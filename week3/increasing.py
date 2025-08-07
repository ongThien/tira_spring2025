def count_sublists(numbers):
    n = len(numbers)
    total = n  # sublists of length 1 are counted too

    i = 1
    cnt = 0
    while i < n:
        if numbers[i] > numbers[i - 1]:
            cnt += 1
        else:
            cnt = 0
        total += cnt
        i += 1

    return total


if __name__ == "__main__":
    print(count_sublists([2, 1, 3, 4]))  # 7
    print(count_sublists([1, 2, 3, 4]))  # 10
    print(count_sublists([4, 3, 2, 1]))  # 4
    print(count_sublists([1, 1, 1, 1]))  # 4
    print(count_sublists([1, 2, 1, 2]))  # 6

    numbers = list(range(1, 10**5 + 1))
    print(count_sublists(numbers))  # 5000050000
