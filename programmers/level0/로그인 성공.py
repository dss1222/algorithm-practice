def solution(id_pw, db):
    for i in db:
        if id_pw[0] == i[0] and id_pw[1] != i[1]:
            return "wrong pw"
        elif id_pw == i:
            return "login"
    return "fail"

def solution2(id_pw, db):
    dic = dict(db)
    if dic.get(id_pw[0],-1) == id_pw[1]:
        return "login"
    elif dic.get(id_pw[0],-1) == -1:
        return "fail"
    else:
        return "wrong pw"

print(solution2(["meosseugi", "1234"], [["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
