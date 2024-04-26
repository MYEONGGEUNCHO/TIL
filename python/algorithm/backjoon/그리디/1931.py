# from pprint import pprint
n = int(input())
# arr =[list(map(int, input().split())) for _ in range(n)]

arr = [[0] * 2 for _ in range(n)]

# pprint(arr)

for i in range(n):
    s, e = list(map(int, input().split()))
    arr[i][0] = e
    arr[i][1] = s

# 정렬
arr.sort()

cnt = 0
s_time = -1
for i in range(n):
    if arr[i][1] >= s_time:
        s_time = arr[i][0] # 종료시간 업뎃
        cnt += 1

print(cnt)


