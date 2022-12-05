def culc(i):
    if i == 0:
        return 1
    else:
        return i * culc(i - 1)


def main():
    n = int(input())
    ans = culc(n)
    print(ans)


if __name__ == "__main__":
    main()
