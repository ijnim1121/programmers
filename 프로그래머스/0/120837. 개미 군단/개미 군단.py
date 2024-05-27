def solution(hp):
    count =0
    list = [5, 3, 1]

    for attack in list:
        count += hp // attack
        hp %= attack
        answer = count
    return answer

