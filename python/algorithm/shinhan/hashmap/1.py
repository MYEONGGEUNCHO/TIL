def solution(participant, completion):
    # 중복체크 - 동명2인 있으면
    check = dict()

    for k in participant:
        if k in check:
            return k
        else:
            check[k] = 1

    # 두 개 리스트 비교 후 없는 인원 뽑기
    answer = ''
    for p in participant:
        if p not in completion:
            return p

