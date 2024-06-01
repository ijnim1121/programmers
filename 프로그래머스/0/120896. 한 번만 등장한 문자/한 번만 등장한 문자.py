def solution(s):
    # 문자열 s에서 각 문자의 빈도수를 계산
    char_count = {} #딕셔너리
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # 한 번만 등장하는 문자를 사전 순으로 정렬하여 문자열로 만들기
    result = ''.join(sorted(char for char, count in char_count.items() if count == 1))
    return result