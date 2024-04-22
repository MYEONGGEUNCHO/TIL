arr:list[str] = [
    '1->4->5',
    '1->3->4',
    '2->6'
]

temp = []
for i in range(len(arr)):
    # 1. 문자열 -> split
    a = arr[i].split('->')
    for j in range(len(a)):
        # 2. 임시 배열 담기
        temp.append(a[j])
# 3. 정렬
a = sorted(temp)
# 4. 정렬 후 다시 문자열로 묶기
print('->'.join(a))