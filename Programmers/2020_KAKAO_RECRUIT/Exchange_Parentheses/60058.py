def correction(br):
    stack = []
    for b in br:
        if b == '(':
            stack.append(b)
        else:
            try:
                stack.pop()
            except:
                return False
    if len(stack) == 0:
        return True
    else:
        return False

# 분기점 만들어주기
def split_brack(br):
    cnt = 0
    for idx in range(len(br)):
        if br[idx] == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return idx + 1
    return idx + 1

def solution(p):
    answer = ''
    if (p == "") or (correction(p) == True):
        return p

    idx = split_brack(p)
    u, v = p[:idx], p[idx:]

    if correction(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        u = u[1:-1].replace('(', 'a')
        u = u.replace(')', 'b')
        u = u.replace('a', ')')
        u = u.replace('b', '(')
        answer = answer + u

    return answer

if __name__ == '__main__' :
    p_1 = "(()())()"
    p_2 = ")("
    p_3 = "()))((()"

    print(solution(p_1))
    print(solution(p_2))
    print(solution(p_3))