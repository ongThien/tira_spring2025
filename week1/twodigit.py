def count_numbers(a, b):
    queue = [2, 5]
    count = 0

    while queue:
        current = queue.pop(0)

        if current > b:
            break  # skip anything above the upper bound

        if a <= current <= b:
            count += 1

        # Generate next numbers
        next1 = current * 10 + 2
        next2 = current * 10 + 5

        queue.append(next1)
        queue.append(next2)

    return count


if __name__ == "__main__":
    print(count_numbers(1, 100))  # 6
    print(count_numbers(60, 70))  # 0
    print(count_numbers(25, 25))  # 1
    print(count_numbers(1, 10**9))  # 1022
    print(count_numbers(123456789, 987654321))  # 512
