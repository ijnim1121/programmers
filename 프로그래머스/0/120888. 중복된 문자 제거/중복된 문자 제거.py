def solution(my_string):
    answer = ''
    stack = []
    for char in my_string:
        if char not in stack:
            stack.append(char)
    answer =''.join(stack)
    return answer