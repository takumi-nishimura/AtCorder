import itertools


def main():
    s = [input() for _ in range(9)]
    ans = 0
    for i1, j1, i2, j2 in itertools.product(range(9), repeat=4):
        if i1 < i2 and j1 <= j2 and s[i1][j1] == "#" and s[i2][j2] == "#":
            di = i2 - i1
            dj = j2 - j1
            i3 = i2 + dj
            j3 = j2 - di
            i4 = i3 - di
            j4 = j3 - dj
            if (
                0 <= i3 < 9
                and 0 <= j3 < 9
                and 0 <= i4 < 9
                and 0 <= j4 < 9
                and s[i3][j3] == "#"
                and s[i4][j4] == "#"
            ):
                ans += 1
    print(ans)


if __name__ == "__main__":
    main()
