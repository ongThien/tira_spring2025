def check_number(number: str) -> bool:
    if number[0] != "0" or len(number) != 9:
        return False

    sum = (
        7 * int(number[1])
        + int(number[2])
        + 3 * int(number[3])
        + 7 * int(number[4])
        + int(number[5])
        + 3 * int(number[6])
        + 7 * int(number[7])
    )

    distance = 0 if sum % 10 == 0 else 10 - (sum % 10)

    return distance == int(number[-1])


if __name__ == "__main__":
    print(check_number("012749138"))  # False
    print(check_number("012749139"))  # True
    print(check_number("013333337"))  # True
    print(check_number("012345678"))  # False
    print(check_number("012344550"))  # True
    print(check_number("1337"))  # False
    print(check_number("0127491390"))  # False
