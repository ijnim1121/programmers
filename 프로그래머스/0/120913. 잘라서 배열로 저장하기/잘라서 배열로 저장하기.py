def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n): #0부터 my_str의 길이까지 n씩 증가
        answer.append(my_str[i:i+n]) # i번째 문자부터 i+n번째 문자까지 슬라이싱한 부분 문자열
    return answer