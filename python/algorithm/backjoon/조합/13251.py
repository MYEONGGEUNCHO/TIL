m = int(input())
arr = list(map(int, input().split()))
k = int(input())

# 구현
total = sum(arr)
res = 0
for i in range(len(arr)):
    if arr[i] < k:
        continue
    else:
        tmp = 1
        tmp_total = total
        tmp_value = arr[i]
        tmp_k = k
        while (tmp_k > 0):
            tmp *= (tmp_value)/tmp_total
            tmp_total -= 1
            tmp_value -= 1
            tmp_k -= 1
        res += tmp
print(res)