def main(argv: str):
    check_1 = not argv.islower()
    check_2 = not argv.isupper()
    check_3 = len(argv) == len(set(argv))
    if check_1 and check_2 and check_3:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main(input())
