def find_number(numbers):
    n = len(numbers)

    i = 1
    while i < n - 1:
        if numbers[i] != numbers[i - 1]:
            if numbers[i] != numbers[i + 1]:
                return numbers[i]
            else:
                return numbers[i - 1]
        i += 1

    return numbers[i]


if __name__ == "__main__":
    print(find_number([1, 1, 1, 2]))  # 2
    print(find_number([1, 1, 2, 1]))  # 2
    print(find_number([1, 2, 1, 1]))  # 2
    print(find_number([2, 1, 1, 1]))  # 2
    print(find_number([5, 5, 5, 3, 5]))  # 3
    print(find_number([1, 100, 1]))  # 100
    print(find_number([1, 5, 5]))  # 1

    numbers = [1] * 10**5 + [2]
    print(find_number(numbers))  # 2
