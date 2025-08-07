def find_distances(street):
    n = len(street)
    d = [0] * n
    shop_index = street.find("1")  # find first shop

    # first pass left to right
    for i in range(n):
        if street[i] == "1":  # update the shop along the way
            shop_index = i

        d[i] = abs(i - shop_index)

    # then pass right to left, comparing the distance both ways
    # to make sure we have the shortest distance
    for i in range(n - 1, -1, -1):
        if street[i] == "1":
            shop_index = i

        d[i] = min(d[i], abs(i - shop_index))
    return d


if __name__ == "__main__":
    print(find_distances("00100010"))  # [2, 1, 0, 1, 2, 1, 0, 1]
    print(find_distances("00100000"))  # [2, 1, 0, 1, 2, 3, 4, 5]
    print(find_distances("11111111"))  # [0, 0, 0, 0, 0, 0, 0, 0]
    print(find_distances("01010101"))  # [1, 0, 1, 0, 1, 0, 1, 0]
    print(find_distances("10000000"))  # [0, 1, 2, 3, 4, 5, 6, 7]
    print(find_distances("00000001"))  # [7, 6, 5, 4, 3, 2, 1, 0]

    # n = 10**5
    # street = "0" * n + "1" + "0" * n
    # distances = find_distances(street)
    # print(distances[1337])  # 98663
