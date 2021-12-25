def solution(msg):
    answer = []
    dic_al = {
        'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6,
        'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12,
        'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
        'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24,
        'Y': 25, 'Z': 26
    }
    dic_size = 26
    buffer = ""
    for al in msg:
        test = buffer + al
        if test in list(dic_al.keys()):
            buffer = test
        else:
            answer.append(dic_al[buffer])
            dic_size += 1
            dic_al[test] = dic_size
            buffer = al
    if buffer:
        answer.append(dic_al[buffer])

    return answer

if __name__ == '__main__':
    msg_1 = "KAKAO"
    msg_2 = "TOBEORNOTTOBEORTOBEORNOT"
    msg_3 = "ABABABABABABABAB"

    print(solution(msg_1))
    print(solution(msg_2))
    print(solution(msg_3))
