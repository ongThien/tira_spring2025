def find_order(n):
    circle = list(range(1, n + 1))
    leave_order = []
    i = 0
    while circle:
        i = (i + 1) % len(circle)
        leave_order.append(circle.pop(i))
        i = i if i < len(circle) else 0

    return leave_order


if __name__ == "__main__":
    print(find_order(1))  # [1]
    print(find_order(2))  # [2, 1]
    print(find_order(3))  # [2, 1, 3]
    print(find_order(7))  # [2, 4, 6, 1, 5, 3, 7]

    order = find_order(10**5)
    print(order[-5:])  # [52545, 85313, 36161, 3393, 68929]
