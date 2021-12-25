def solution(s):
    stack = []

    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)

    for i in s :
        spy = i.split(',')
        for j in spy :
            if not int(j) in stack :
                stack.append(int(j))
    return stack


if __name__ == '__main__' :
    s_1 = {{2},{2, 1},{2, 1, 3},{2, 1, 3, 4}}
    s_2 = {{1, 2, 3},{2, 1},{1, 2, 4, 3},{2}}
    s_3 = {{20, 111},{111}}
    s_4 = {{123}}
    s_5 = {{4, 2, 3},{3},{2, 3, 4, 1},{2, 3}}

    # print(solution(s_1))
    # print(solution(s_2))
    # print(solution(s_3))
    # print(solution(s_4))
    # print(solution(s_5))