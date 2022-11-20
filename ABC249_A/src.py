def calc(p, q, r):
    return p * q * (x // (p + r)) + q * min(p, x % (p + r))


def main(argv):
    global x
    a, b, c, d, e, f, x = map(int, argv)
    tak = calc(a, b, c)
    aok = calc(d, e, f)
    if tak == aok:
        print("Draw")
    elif tak > aok:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    main(input().split())
