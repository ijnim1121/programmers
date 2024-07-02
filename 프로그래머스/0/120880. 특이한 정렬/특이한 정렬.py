def solution(numlist, n):
    answer = []
    # n과의 거리를 계산하고, 거리가 같다면 더 큰 수를 앞에 오도록 정렬
    answer = sorted(numlist, key=lambda x: (abs(x - n), -x))
    return answer