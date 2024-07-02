def solution(score):
    answer = []
    avg_scores = []
    
    # 각 학생의 평균 점수 계산
    for eng, math in score:
        avg_scores.append((eng + math) / 2)
    
    # 평균 점수를 내림차순으로 정렬
    sorted_avg_scores = sorted(avg_scores, reverse=True)
    
    # 각 학생의 평균 점수를 sorted_avg_scores 리스트에서 찾아 그 인덱스에 1을 더해 등수를 계산
    for student_avg in avg_scores:
        answer.append(sorted_avg_scores.index(student_avg) + 1)
    
    return answer