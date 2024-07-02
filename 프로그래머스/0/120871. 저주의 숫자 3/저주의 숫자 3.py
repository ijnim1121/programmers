def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer
#파이썬에서는 반복을 수행하되, 변수 값이 필요 없을 때 언더바(_)를 사용할 수 있다.