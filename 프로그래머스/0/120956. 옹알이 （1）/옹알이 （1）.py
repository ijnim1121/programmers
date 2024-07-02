def solution(babbling):
    count = 0
    patterns = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        temp = word
        for pattern in patterns:
            if pattern in temp:
                temp = temp.replace(pattern, " ")
        if temp.strip() == "":
            count += 1
    
    return count