def solution(before, after):
    # before의 문자들을 리스트로 변환하고 정렬
    before_list = sorted(list(before))
    
    # after의 문자들을 리스트로 변환하고 정렬
    after_list = sorted(list(after))

    if before_list == after_list:
        answer = 1
    else:
        answer = 0
        
    return answer