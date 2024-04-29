import math

n, m, k = map(int, input().split())



numCases = math.perm(n + m, n + m) / (math.perm(n, n) * math.perm(m, m))

if k > numCases:
    print(-1)

