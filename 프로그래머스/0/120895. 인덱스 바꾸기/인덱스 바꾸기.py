def solution(my_string, num1, num2):
    answer = ''
    my_list = list(my_string)
    temp = my_list[num1]
    my_list[num1] = my_list[num2]
    my_list[num2] = temp
    answer = ''.join(map(str, my_list))
    return answer 