n = int(input())

DP = [0] * (n+3) # n 값 떄문

DP[1] = 1
DP[2] = 2

if n > 2:
    for i in range(3, n+1):
        DP[i] = DP[i-1] + DP[i-2]

print(DP[n] % 10007)