def solution_fail(s):
    s = list(s)
    for i in range(len(s)) :
        for j in range(i + 1, len(s)) :
            if s[i] == '(' and s[j] == ')' :
                s[i], s[j] = 'X', 'X'
                break

    s = list(set(s))
    # print(len(s))

    if len(s) - 1 != 0 :
        return False
    else:
        return True

def solution(s):
    stack = []
    for paren in s :
        if paren == '(' :
            stack.append(paren)
        else :
            if len(stack) == 0 :
                return False
            else :
                stack.pop()

    if len(stack) == 0 :
        return True
    else :
        return False

    # return True

if __name__ == '__main__' :
    s_1 = "()()"
    s_2 = "(())()"
    s_3 = ")()("
    s_4 = "(()("

    print(solution(s_1))
    print(solution(s_2))
    print(solution(s_3))
    print(solution(s_4))