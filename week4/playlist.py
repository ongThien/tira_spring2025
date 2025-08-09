def count_parts(songs: list[int]) -> int:
    n = len(songs)
    seen = set()
    cnt = 0
    l, r = 0, 0

    while r < n:
        while songs[r] in seen:
            seen.remove(songs[l])
            l += 1
        seen.add(songs[r])
        cnt += r - l + 1
        r += 1

    return cnt


if __name__ == "__main__":
    print(count_parts([1, 1, 1, 1]))  # 4
    print(count_parts([1, 2, 3, 4]))  # 10
    print(count_parts([1, 2, 1, 2]))  # 7
    print(count_parts([1, 2, 1, 3]))  # 8
    print(count_parts([1, 1, 2, 1]))  # 6

    songs = [1, 2] * 10**5
    print(count_parts(songs))  # 399999
    songs = list(range(1, 10**5 + 1)) * 2
    print(count_parts(songs))  # 15000050000
