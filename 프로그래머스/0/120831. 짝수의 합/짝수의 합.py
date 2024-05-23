def solution(n):
    sum_even = 0
    for i in range(2, n+1, 2):  # 2부터 시작하여 n까지 2씩 증가시키며 반복
        sum_even += i
    return sum_even