from pprint import pprint
n, r = map(int, input().split())
# print(n, r)
DP = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    DP[i][0] = 1
    DP[i][i] = 1
    DP[i][1] = i

for i in range(1, n+1):
    for j in range(1, n+1):
        DP[i][j] = DP[i-1][j] + DP[i-1][j-1]

print(DP[n][r]%10007)