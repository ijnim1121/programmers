def solution(id_pw, db):
    answer = ''
    id1 = id_pw[0]
    pw = id_pw[1]
    for i in range(len(db)):
        if id1 == db[i][0]:
            if pw == db[i][1]:
                answer = "login"
                break
            else:
                answer = "wrong pw"
                break
        else:
            answer = "fail"
    return answer