def solution(n, control):
    answer = n
    for i in range(len(control)):
        if control[i] == 'w':
            answer += 1
        elif control[i] == 's':
            answer -= 1
        elif control[i] == 'd': 
            answer += 10
        elif control[i] == 'a':
            answer -= 10
            
    return answer

n = 0
control = "wsdawsdassw"	

print(solution(n, control))