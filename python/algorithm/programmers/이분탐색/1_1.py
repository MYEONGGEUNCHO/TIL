def solution(n, times):
    answer = 0

    left = min(times)
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2
        # print(mid)
        checked_person = 0
        for time in times:
            checked_person += mid//time

            if checked_person >= n:
                break
        
        if checked_person >= n:
            answer = mid
            right = mid - 1

        elif checked_person < n:
            left = mid + 1

    return answer

n = 6
times = [7, 10]
print(solution(n, times))