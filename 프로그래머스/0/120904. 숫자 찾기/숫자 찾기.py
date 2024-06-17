def solution(num, k):
    answer = 0
    str_num = str(num)
    str_k = str(k)
    for n in range(len(str_num)):
        if str_num[n] == str_k:
            answer = n+1
            break
        else:
            answer = -1
    return answer