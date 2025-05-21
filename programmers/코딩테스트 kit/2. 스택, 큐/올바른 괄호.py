#https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):

    if s[0] == ")" or s[-1] == "(":
        return False
    open_count = 0

    for i in s:
        if i == "(":
            open_count += 1
        else:
            open_count -= 1
        
        if open_count < 0:
            return False
    
    if open_count == 0:
        return True
    
    return False

print(solution("()()"))

def solution_example(s):
    st = list()
    for c in s:
        if c == "(":
            st.append(c)

        if c == ")":
            try:
                st.pop()
            except IndexError:
                return False
    
    return len(st) == 0