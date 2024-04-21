def solution(num_list):
    answer = 0
    mul = 1
    for num in num_list:
        mul *= num
        answer += (num**2)

    if answer <= mul:
        return 0
    
    return 1

num_list = [3, 4, 5, 2, 1]

print(solution(num_list))