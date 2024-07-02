def solution(num, total):
    # 연속된 num개의 수를 더했을 때 total이 되는 시작값 계산(등차수열 합 공식)
    start = (total - num * (num - 1) // 2) // num
    
    # 시작값부터 num개의 연속된 수를 생성
    answer = [start + i for i in range(num)]
    
    return answer