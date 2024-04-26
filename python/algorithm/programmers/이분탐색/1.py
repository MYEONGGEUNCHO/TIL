from pprint import pprint
def solution(n, times):
    answer = 0
    m = len(times)

    arr = list()

    for i in range(n * m):
        for j in range(m):
            arr.append([(i+1)*times[j], i * times[j]])
    arr.sort()
    # pprint(arr)
    answer = arr[n - 1][0]
    return answer

n = 6
times = [7, 10]

print(solution(n, times))