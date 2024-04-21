def solution(phoneBook):
    phoneBook.sort()

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1, p2)
        # if p2.startswith(p1):
        #     return False
    return True

phoneBook = ["12","123","1235","567","88"]
solution(phoneBook)