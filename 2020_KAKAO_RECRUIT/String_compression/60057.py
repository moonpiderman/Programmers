def solution(s):
    length = []
    string = ""

    if len(s) == 1 :
        return 1

    for trim in range(1, len(s) // 2 + 1) :
        count = 1
        tmp = s[:trim]
        for i in range(trim, len(s), trim) :
            # 같은 구간만큼 체크
            if s[i : i+trim] == tmp :
                count += 1
            else :
                if count == 1:
                    # 하나 짜리는 카운팅해줄 필요 없음
                    count = ""
                string += str(count) + tmp
                tmp = s[i : i+trim]
                count = 1
        if count == 1 :
            count = ""
        string += str(count) + tmp
        length.append(len(string))
        string = ""

    return min(length)

if __name__ == '__main__' :
    s_1 = "aabbaccc"
    s_2 = "ababcdcdababcdcd"
    s_3 = "abcabcdede"
    s_4 = "abcabcabcabcdededededede"
    s_5 = "xababcdcdababcdcd"

    print(solution(s_2))