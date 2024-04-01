from typing import List
num_dict = {
    '0' : ['O', '()', '0'],
    '1' : ['I', '1'],
    '2' : ['Z', 'S', '7_', '2'],
    '3' : ['E', 'B', '3'],
    '4' : ['A', '4'],
    '5' : ['Z', 'S', '5'],
    '6' : ['b', 'G', '6'],
    '7' : ['T', 'Y', '7'],
    '8' : ['B', 'E3', '8'],
    '9' : ['g', 'q', '9']
}

str_dict = {
    'O': '0', 
    '()': '0', 
    'I': '1', 
    'Z': ['2', '5'],
    'S': ['2', '5'], 
    '7_': '2', 
    'E': '3',
    'B': ['3', '8'], 
    'A': '4', 
    'b': '6', 
    'G': '6', 
    'T': '7', 
    'Y': '7', 
    'B': '8', 
    'E3': '8', 
    'g': '9', 
    'q': '9'
}

def next_word():
    pass

def check(numstr:str, word: str, idx: int) -> bool:
    res = []
    cnt = 0
    for alpabet in numstr:
        if alpabet == num_dict[idx]:
            res.append(idx)
        else:
            cnt += 1
    return False
    


def solution(numstrs: List[str], words: List[str]):
    
    res: list = []
    for word in words:
        cnt: int = 0
        for numstr in numstrs:
            idx = len(numstr)
            word_length = len(word)
            if len(word) > len(numstr):
                res.append(0)
            else:
                if check(numstr=numstr, word=word, idx=idx):
                    pass

            # 다른 키에 같은 문자X

            # 같은 키에 다른 문자O


                
                
x = ['ZASSETE', 'S4Z537B', '7_ASZEYB']

# y = ['2455373', '425', '373', '378']
y = ['425']

print(solution(x, y))