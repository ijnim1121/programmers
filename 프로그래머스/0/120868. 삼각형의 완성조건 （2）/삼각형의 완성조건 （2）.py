def solution(sides):
    answer = 0
    max_side = max(sides)
    min_side = min(sides)
    
    # 가장 긴 변이 sides 배열 안에 있는 경우
    for i in range(max_side - min_side + 1, max_side + 1):
        answer += 1
    
    # 가장 긴 변이 sides 배열 밖에 있는 경우
    for i in range(max_side+1, min_side+max_side):
        answer += 1
    
    return answer