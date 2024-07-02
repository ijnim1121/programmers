import math

def solution(a, b):
    answer = 0
    gcd = math.gcd(a, b)
    new_a = a//gcd
    new_b = b//gcd
    
    # 분모의 소인수가 2와 5만 존재하는지 확인
    while new_b % 2 == 0:
        new_b //= 2
    while new_b % 5 == 0:
        new_b //= 5
    if new_b == 1:
        answer = 1
    else:
        answer =2
    
    return answer