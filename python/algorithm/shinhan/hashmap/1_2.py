def solution(participant, completion):
    answer = ''
    check = dict()

    # 중복체크 key point
    for player in participant:
        if player in check:
            check[player] += 1
        else:
            check[player] = 1
    for player in completion:
        if player in check:
            check[player] -= 1
    
    
    for player, values in check.items():
        if values != 0:
            return player

participant =  ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]

print(solution(participant, completion))