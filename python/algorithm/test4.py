from typing import List
num_dict = {
    '0' : ['O', '()'],
    '1' : 'I',
    '2' : ['Z', 'S', '7_'],
    '3' : ['E', 'B'],
    '4' : 'A',
    '5' : ['Z', 'S'],
    '6' : ['b', 'G'],
    '7' : ['T', 'Y'],
    '8' : ['B', 'E3'],
    '9' : ['g', 'q']
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


def check(k: str):

    if k in num_dict[k]:
        return num_dict[k]



def solution(numstrs: List[str], words: List[str]):
    
    for numstr in numstrs:
        for word in words:
            res: list = []
            for key in word:
                if numstr.find(key):
            # 숫자가 dict에 있는지 확인
                    if key in num_dict:
                        # 단어 조합
                        mid_temp: List[str] =  [] # 임시 문자열 보관함
                        for alphabet in num_dict[key]:
                            temp = []
                            # 이미 알파벳이 있으면
                            if len(temp) > 1:
                                # 기존 알파벳에 더하기
                                for _ in temp:
                                    _ += alphabet

                                    temp.append(_)
                            elif len(temp) == len(word):
                                mid_temp = temp
                            else:
                                temp.append(alphabet)
                        # 안되는 조건
    
                
                
x = ['ZASSETE', 'S4Z537B', '7_ASZEYB']

# y = ['2455373', '425', '373', '378']
y = ['425']

solution(x, y)