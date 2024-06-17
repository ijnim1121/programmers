def valid(equation):
    equation = equation.replace('=', '==')
    return eval(equation)
#eval: 문자열 형태의 Python 코드를 실행하여 그 결과를 반환

def solution(equations):
    return ["O" if valid(equation) else "X" for equation in equations]