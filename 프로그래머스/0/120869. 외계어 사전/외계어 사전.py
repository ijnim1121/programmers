def solution(spell, dic):
    answer = 0
    for word in dic:
        if len(word) == len(set(word)) and set(spell) == set(word):
            answer = 1
            break
    else:
        answer = 2
    return answer

#len(word) == len(set(word)) 조건을 통해 단어 내부의 알파벳이 중복되지 않는지 확인
#set(spell) == set(word) 조건을 통해 spell에 담긴 알파벳과 단어 내부의 알파벳이 동일한지 확인