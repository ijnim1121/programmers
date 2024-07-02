def solution(dots):
    # 가로 길이 구하기
    x_coords = [dot[0] for dot in dots]
    width = max(x_coords) - min(x_coords)
    
    # 세로 길이 구하기
    y_coords = [dot[1] for dot in dots]
    height = max(y_coords) - min(y_coords)
    
    # 넓이 계산
    answer = width * height
    
    return answer