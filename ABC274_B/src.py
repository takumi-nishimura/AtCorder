def main():
    h, w = map(int, input().split())
    x = [0] * w
    for _ in range(h):
        c = input()
        for i in range(w):
            if c[i] == "#":
                x[i] += 1
    print(*x)


if __name__ == "__main__":
    main()
