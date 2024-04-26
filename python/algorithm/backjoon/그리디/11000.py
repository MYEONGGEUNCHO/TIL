# 강의실 배정 - 우선순위 큐
# from pprint import pprint
import sys
import heapq
input = sys.stdin.readline

n = int(input())
arr = [[0] * 2 for _ in range(n)]

for i in range(n):
    s, e = list(map(int, input().split()))
    arr[i][0] = s
    arr[i][1] = e
# pprint(arr)
arr.sort(key=lambda x : (x[0],x[1]))

# 회의실은 가장 빨리 시작하는 순으로 정렬한다.
# 그래야 heap을 강의 끝나는 시간을 갱신할때, 다른 비교없이 heappop만으로 끝낼 수 있기 때문이다.

heap = [arr[0][1]]
for i in range(1,n):
    if heap[0] <= arr[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap,arr[i][1])

print(len(heap))