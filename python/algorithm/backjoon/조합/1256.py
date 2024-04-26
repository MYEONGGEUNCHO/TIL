import math
# from pprint import pprint
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

# DP테이블 세팅
DP = [[0 for _ in range(n+m+2)] for _ in range(n+m+2)]

# 기본값 세팅
for i in range(n+m+2):
    # DP[0][i] = 0
    DP[i][0] = 1
    DP[i][i] = 1

# DP테이블 채우기
for i in range(2, n+m+2):
    for j in range(1, n+m+2):
        DP[i][j] = DP[i-1][j-1] + DP[i-1][j]

# pprint(DP)

numCases = math.perm(n+m, n+m) /(math.perm(n,n) * math.perm(m,m))

if k > numCases:
    print(-1)
else:
    # 반복 조건이 중요
    while (m >= 0 and (n-1+m >= 0)):
        if DP[n-1+m][m] >= k:
            print("a", end="")
            n -= 1
        else:
            print("z", end="")
            k -= DP[n-1+m][m]
            m -= 1