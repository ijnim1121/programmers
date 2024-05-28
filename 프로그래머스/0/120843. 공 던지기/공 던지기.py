def solution(numbers, k):
    index = 0
    for i in range(k):
        index = ((k-1)*2) % len(numbers)
    return numbers[index]