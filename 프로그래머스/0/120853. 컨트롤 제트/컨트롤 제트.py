def solution(s):
    answer = 0
    s_list = s.split(' ')
    stack = []
    for item in s_list:
        if item == "Z" and stack:
            answer -= stack.pop()
        else:
            num = int(item)
            answer += num
            stack.append(num)
    return answer