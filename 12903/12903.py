def solution(s):
    str_len = len(s)

    if int(str_len % 2) == 1:
        answer = s[str_len//2]

    elif int(str_len % 2) == 0:
        answer = s[(str_len//2) - 1] + s[str_len//2]

    return answer
