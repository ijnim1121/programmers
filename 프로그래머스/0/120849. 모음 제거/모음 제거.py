def solution(my_string):
    delete = "aeiou"  # 제거해야 할 모음 문자들
    answer = ''
    for char in my_string:
        if char not in delete:
            answer += char
    return answer