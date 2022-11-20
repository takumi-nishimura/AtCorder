import collections
import itertools


def calc(pair):
    C = collections.Counter()
    for i in range(N):
        if pair[i]:
            for j in S[i]:
                C[j] += 1
    score = 0
    for _, q in C.items():
        if q == K:
            score += 1
    return score


def main():
    global N, K, S
    N, K = map(int, input().split())
    S = [input() for _ in range(N)]
    ans = 0
    for pair in itertools.product((True, False), repeat=N):
        ans = max(ans, calc(pair))
    print(ans)


if __name__ == "__main__":
    main()
