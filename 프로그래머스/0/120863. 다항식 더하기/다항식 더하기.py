def solution(polynomial):
    # 다항식을 분리하여 각 항의 계수와 변수를 추출
    terms = polynomial.split(" + ")
    x_coef = 0
    const = 0
    for term in terms:
        if "x" in term:
            if term == "x":
                x_coef += 1
            else:
                x_coef += int(term[:-1])
        else:
            const += int(term)
    
    # 동류항끼리 계수를 더함
    result = ""
    if x_coef > 0:
        if x_coef == 1:
            result += "x"
        else:
            result += str(x_coef) + "x"
    if const > 0:
        if result:
            result += " + " + str(const)
        else:
            result = str(const)
    
    return result