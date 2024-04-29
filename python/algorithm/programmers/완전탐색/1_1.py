
import math
def solution(brown, yellow):
    ans=((brown-4)+math.sqrt((brown-4)**2-16*yellow))//4
    return [ans+2,yellow//ans+2]