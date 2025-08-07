def count_sublists(numbers):
    n = len(numbers)
    cur_cnt = 0
    total = 0
    for num in numbers:
        if num % 2 == 0:
            cur_cnt += 1
        else:
            total += cur_cnt * (cur_cnt + 1) // 2
            cur_cnt = 0

    # case where numbers end with an even num
    total += cur_cnt * (cur_cnt + 1) // 2

    return total


if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6]))  # 4
    print(count_sublists([1, 2, 3, 4]))  # 2
    print(count_sublists([1, 1, 1, 1]))  # 0
    print(count_sublists([2, 2, 2, 2]))  # 10
    print(count_sublists([1, 1, 2, 1]))  # 1

    numbers = [2] * 10**5
    print(count_sublists(numbers))  # 5000050000
