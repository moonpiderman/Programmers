def solution(s):
    stack = []

    for alpha in s :
        if len(stack) == 0 :
            stack.append(alpha)
        elif stack[-1] == alpha :
            stack.pop()
        else :
            stack.append(alpha)

    if len(stack) == 0 :
        return 1
    else :
        return 0

if __name__ == '__main__' :
    s_1 = "baabaa"
    s_2 = "cdcd"

    print(solution(s_1))
    print(solution(s_2))