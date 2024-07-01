def solution(array):
    answer = 0
    str1 = ''.join(str(s) for s in array)
    for i in str1:
        if i == '7':
            answer += 1
    return answer