def solution(array):
    array.sort()
    mid=(len(array)//2)
    answer = array[mid]
    return answer