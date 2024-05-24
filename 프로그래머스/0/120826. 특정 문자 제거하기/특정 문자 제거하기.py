def solution(my_string, letter):
    # replace 메서드를 사용하여 letter를 제거
    new_string = my_string.replace(letter, '')
    return new_string