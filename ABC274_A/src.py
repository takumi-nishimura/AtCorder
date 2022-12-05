from decimal import Decimal, ROUND_HALF_UP


def main():
    a, b = map(int, input().split())
    s = b / a
    print(Decimal(str(s)).quantize(Decimal("0.001"), rounding=ROUND_HALF_UP))


if __name__ == "__main__":
    main()
