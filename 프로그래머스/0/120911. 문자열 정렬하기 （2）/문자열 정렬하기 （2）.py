def solution(my_string):
    answer = ''
    my_string_lower = my_string.lower()
    answer = ''.join(sorted(my_string_lower))
    return answer