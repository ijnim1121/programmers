def solution(common):
    n = len(common)
    
    # 등차수열 판별
    if common[1] - common[0] == common[2] - common[1]:
        return common[-1] + (common[1] - common[0])
    # 등비수열 판별
    elif common[1] / common[0] == common[2] / common[1]:
        return common[-1] * (common[1] / common[0])
    
    # 그 외의 경우
    return -1