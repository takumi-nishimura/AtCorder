def main():
    n = int(input())
    h = list(map(int, input().split()))
    _a = max(h)
    for i, j in enumerate(h):
        if j == _a:
            print(i + 1)


if __name__ == "__main__":
    main()
