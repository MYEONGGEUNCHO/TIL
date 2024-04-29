k = int(input())

for _ in range(k):
    n = int(input())
    r = int(input())

    DP = [[0 for _ in range(15)] for _ in range(15)]

    # 기본값 세팅

    for i in range(1, 15):
        DP[0][i] = i
        DP[i][0] = 0
        DP[i][1] = 1

    for i in range(1, 15):
        for j in range(2, 15):
            DP[i][j] = DP[i-1][j] + DP[i][j-1]

    print(DP[n][r])