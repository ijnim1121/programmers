def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]
# [numbers[-1]] + numbers[:-1]는 리스트의 마지막 요소를 첫 번째 위치로 이동시키고 나머지 요소들을 뒤따라오게 함
# numbers[1:] + [numbers[0]]는 리스트의 첫 번째 요소를 마지막 위치로 이동시키고 나머지 요소들을 앞에 위치시킴