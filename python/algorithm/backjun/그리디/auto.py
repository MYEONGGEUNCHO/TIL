from queue import PriorityQueue

n = 10
k = 3
m = 7

# 각 사람당 가방의 최대 무게
limit_per_person = m

arr = [
    [4, 5],
    [3, 4],
    [2, 1],
    [5, 7],
    [1, 1],
    [7, 8],
    [8, 6],
    [3, 3],
    [4, 3],
    [5, 4],
]

# (가치, 무게) 형식으로 우선순위 큐를 사용하여 최대 가치를 계산
pq = PriorityQueue()

# 모든 아이템을 가치 기준으로 정렬하여 우선순위 큐에 넣기
for weight, value in arr:
    pq.put((-value, weight))

total_value = 0

# 각 사람의 가방을 채우기 위해 k번 반복
for _ in range(k):
    individual_weight = 0
    individual_value = 0
    
    temp_items = []
    
    while not pq.empty() and individual_weight < limit_per_person:
        value, weight = pq.get()
        value = -value
        
        if individual_weight + weight <= limit_per_person:
            individual_weight += weight
            individual_value += value
        else:
            # 나중에 다시 넣을 수 있도록 저장
            temp_items.append((value, weight))
    
    # 우선순위 큐에 다시 아이템을 추가
    for item in temp_items:
        pq.put((-item[0], item[1]))
    
    total_value += individual_value

print(f"최대 가치: {total_value}")
