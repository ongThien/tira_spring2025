def create_distribution(string):
    n = len(string)
    substrings = set()
    dist = {}

    for i in range(n):
        for j in range(i, n):
            cur = string[i : j + 1]
            if cur not in substrings:
                substrings.add(cur)
                if len(cur) in dist:
                    dist[len(cur)] += 1
                else:
                    dist[len(cur)] = 1

    return dist


if __name__ == "__main__":
    print(create_distribution("aaaa"))
    # {1: 1, 2: 1, 3: 1, 4: 1}

    print(create_distribution("abab"))
    # {1: 2, 2: 2, 3: 2, 4: 1}

    print(create_distribution("abcd"))
    # {1: 4, 2: 3, 3: 2, 4: 1}

    print(create_distribution("abbbbbb"))
    # {1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 1}

    print(create_distribution("aybabtu"))
    # {1: 5, 2: 6, 3: 5, 4: 4, 5: 3, 6: 2, 7: 1}
