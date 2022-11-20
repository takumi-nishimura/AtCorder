def main():
    N = int(input())
    S = [input() for _ in range(N)]
    s1 = "HDCS"
    s2 = "A23456789TJQK"
    s1 = list(map(str, s1))
    s2 = list(map(str, s2))
    s1_r = False
    s2_r = False
    s3_r = True
    for i in S:
        for j in s1:
            if j in i[0]:
                s1_r = True
        for k in s2:
            if k in i[1]:
                s2_r = True
    for p in range(N):
        for q in range(p):
            if S[p] == S[q]:
                s3_r = False

    if s1_r and s2_r and s3_r:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
