import math
def solution(users: list[list[int]], emoticons: list[int]):
    answer = []
    for user in users:
        disc = math.ceil(user[0]/10)/10
        print(disc)
        user[1]
    return answer


users = [[40, 10000], [25, 10000]]

emoticons = [7000, 9000]

print(solution(users, emoticons))