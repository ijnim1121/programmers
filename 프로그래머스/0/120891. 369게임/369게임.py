def solution(order):
    answer = 0
    for a in str(order):
        if a in ['3', '6', '9']:
            answer += 1
    return answer