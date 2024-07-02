def solution(bin1, bin2):
    # 이진수를 10진수로 변환
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    
    # 두 10진수의 합 계산
    result = num1 + num2
    
    # 결과를 다시 이진수로 변환
    return bin(result)[2:]