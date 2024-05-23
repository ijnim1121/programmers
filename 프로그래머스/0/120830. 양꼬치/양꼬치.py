def solution(n, k):
    sum = (n*12000)+(k*2000)
    sum = sum-((n//10)*2000)
    return sum