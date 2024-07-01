def solution(numbers):
    # numbers 배열에서 가장 큰 두 개의 수를 찾아서 곱한다.
    sorted_numbers = sorted(numbers, reverse=True)
    max1 = sorted_numbers[0]
    max2 = sorted_numbers[1]
    
    # 가장 작은 두 개의 수를 곱한 값과 비교하여 더 큰 값을 반환한다.
    sorted_numbers_F = sorted(numbers, reverse=False)
    min1 = sorted_numbers_F[0]
    min2 = sorted_numbers_F[1]
    
    return max(max1 * max2, min1 * min2)