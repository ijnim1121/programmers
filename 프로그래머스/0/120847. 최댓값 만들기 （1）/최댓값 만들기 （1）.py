import math
def solution(numbers):
    asc = sorted(numbers, reverse=True)
    answer = asc[0]*asc[1]
    return answer