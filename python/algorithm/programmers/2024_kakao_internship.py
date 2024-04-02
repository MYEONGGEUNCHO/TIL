from typing import List, Dict
def solution(friends: List[str], gifts: List[str]) -> int:
    # gifts => A B: str, A(준 사람): +1 B(받은 사람): -1 => 선물지수
    give_list = dict() # {기록자: {선물준 사람: 준 개수}}, 준 개수만 체크
    gift_index = dict()
    for friend in friends:
        give_list[friend] = dict()
        gift_index[friend] = 0
    for gift in gifts:
        A, B = gift.split(' ')
        # 기존에 있으면 += 1
        if B in give_list[A]:
            give_list[A][B] += 1
        # 리스트 최초 등록은 1
        else:
            give_list[A][B] = 1
        # 주면 +1 받으면 -1
        gift_index[A] += 1
        gift_index[B] -= 1

    # 점수계산 로직
    score = [0 for _ in friends]
    for i in range(len(friends)):
        A = friends[i]
        for j in range(i+1, len(friends)):
            B = friends[j]
            a = give_list[A][B] if B in give_list[A] else 0
            b = give_list[B][A] if A in give_list[B] else 0

            if a > b:
                score[i] += 1
            elif a < b:
                score[j] += 1
            elif a == b:
                a_gift_index, b_gift_index = gift_index[A], gift_index[B]
                if a_gift_index > b_gift_index:
                    score[i] += 1
                elif a_gift_index < b_gift_index:
                    score[j] += 1
    answer = max(score)
    return answer

# friends = ["joy", "brad", "alessandro", "conan", "david"]
friends = ["a", "b", "c"]

# gifts = ["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
gifts = ["a b", "b a", "c a", "a c", "a c", "c a"]

print(solution(
    friends=friends
    , gifts=gifts
))