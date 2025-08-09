def hash_value(string):
    A = 23
    M = 2**32
    n = len(string)

    value = 0
    for ch in string:
        value += coded(ch) * (A ** (n - 1))
        n -= 1

    return value % M


def coded(char):
    return ord(char) - 97


if __name__ == "__main__":
    print(hash_value("abc"))  # 25
    print(hash_value("kissa"))  # 2905682
    print(hash_value("aybabtu"))  # 154753059
    print(hash_value("tira"))  # 235796
    print(hash_value("zzzzzzzzzz"))  # 2739360440
