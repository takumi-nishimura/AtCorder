def main():
    S = input()
    n = None
    for i, j in enumerate(S):
        if "a" == j:
            n = i + 1
    if n:
        print(n)
    else:
        print(-1)


if __name__ == "__main__":
    main()
