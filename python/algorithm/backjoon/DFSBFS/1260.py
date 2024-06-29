from pprint import pprint
n, m, k = map(int, input().split())

arr = []
for _ in range(m):
    a, b = map(int, input().split())

    arr.append((a, b))

visited = [False] * m
stack = []
