def sorting(phone_book: list[str]):
    phone_book.sort(key=len)
    return phone_book

def solution(phone_book):
    answer = True
    arrs = sorting(phone_book)
    n = len(phone_book)
    for i in range(n):
        for j in range(i+1, n):
            if arrs[i] == arrs[j][:len(arrs[i])]:
                return False        
    
    return answer

# phone_book = ["119", "97674223", "1195524421"]
# phone_book = ["123","456","789"]
phone_book = ["12","123","1235","567","88"]	
print(solution(phone_book))