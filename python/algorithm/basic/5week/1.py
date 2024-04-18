def solution(code):
    answer = ''
    mode = 0
    n = len(code)
    for i in range(n):
        if code[i] == '1':
            if mode == 0:
                mode = 1
            elif mode == 1:
                mode = 0
            continue
        if mode == 0:
            if i % 2 == 0:
                answer += code[i]
        elif mode == 1:
            if i % 2 != 0:
                answer += code[i]
                
    if answer == "":
        return "EMPTY"
    return answer

print(solution('abc1abc1abc'))