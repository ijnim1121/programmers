def solution(array, n):
    answer = array[0] # 배열의 첫 번째 요소를 초기값으로 설정
    min_diff = abs(array[0] - n) # 첫 번째 요소와 n의 차이를 초기값으로 설정

    for i in range(1, len(array)):
        diff = abs(array[i] - n)
        if diff < min_diff:
            min_diff = diff
            answer = array[i]
        elif diff == min_diff:
            answer = min(answer, array[i])

    return answer