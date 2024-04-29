def com_div(square):
    ans = list()
    for i in range(1, square+1):
        mogs =  square // i # 몫
        if square % i == 0 and mogs <= i:
            ans.append((i, mogs))
    return ans

def solution(brown: int, yellow: int):
    answer = []
    square = brown + yellow
    # square의 공약수

    com_list = com_div(yellow)

    for com in com_list:
        x = com[0]
        y = com[1]

        brown = (x+2)*2 + (y*2)
        a = x+2
        b = y+2
        if square == a*b:
            return [a, b]

brown = 24
yellow = 24

print(solution(brown, yellow))