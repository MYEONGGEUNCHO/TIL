n = int(input())


DP = [0]*(n+4) # n=1일떄 index error 방지

# 기본값 세팅
DP[0] = 0
DP[1] = 0
DP[2] = 1
DP[3] = 1

if n > 3:
    for i in range(4, n+1):
        if i % 3 == 0 and i % 2 == 0:
            DP[i] = min(DP[i-1], DP[i//3], DP[i//2]) + 1    
        elif i % 3 == 0:
            DP[i] = min(DP[i-1], DP[i//3]) + 1
        elif i % 2 == 0:
            DP[i] = min(DP[i-1], DP[i//2]) + 1
        elif i % 3 != 0 and i % 2 != 0:
            DP[i] = DP[i-1] + 1

print(DP[n])