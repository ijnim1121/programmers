def solution(my_string):
    answer = []
    for char in my_string:
        if char.isdigit():  # char가 숫자인지 확인
            answer.append(int(char))  # char를 정수로 변환하여 answer에 추가
    answer.sort()  # answer 리스트를 오름차순으로 정렬
    return answer