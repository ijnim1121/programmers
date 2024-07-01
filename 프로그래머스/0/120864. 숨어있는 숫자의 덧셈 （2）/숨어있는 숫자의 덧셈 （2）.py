def solution(my_string):
    answer = 0
    num = 0
    
    for char in my_string:
        if char.isdigit():
            num = num * 10 + int(char)
        else:
            if num != 0:
                answer += num
                num = 0
    
    return answer + num