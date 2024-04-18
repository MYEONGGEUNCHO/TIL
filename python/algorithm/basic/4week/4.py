def solution(ineq, eq, n, m):
    answer = 0
    if ineq == '>':
        if eq == '=':
            if n >= m:
                return 1
            else:
                return 0
        elif eq == '!':
            if n > m:
                return 1
            else:
                return 0
    elif ineq == '<':
        if eq == '=':
            if n <= m:
                return 1
            else:
                return 0
        elif eq == '!':
            if n < m:
                return 1
            else:
                return 0