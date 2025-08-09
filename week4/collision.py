def hash_value(string):
    A = 23
    M = 2**32
    n = len(string)

    value = 0
    for ch in string:
        value += (ord(ch) - 97) * (A ** (n - 1))
        n -= 1

    return value % M

def find_other(string):
    # TODO

if __name__ == "__main__":
    string1 = "kissa"
    string2 = find_other("kissa")
    print(string1, hash_value(string1)) # kissa 2905682
    print(string2, hash_value(string2)) # zfgjynuk 2905682
