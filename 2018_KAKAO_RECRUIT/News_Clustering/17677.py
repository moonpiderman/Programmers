def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    str1_re = []
    str2_re = []

    # str1 쪼개기
    for i in range(len(str1) - 1) :
        tmp = ""
        if str1[i].isalpha() and str1[i + 1].isalpha() :
            tmp += str1[i]
            tmp += str1[i + 1]
            str1_re.append(tmp)
    # str2 쪼개기
    for i in range(len(str2) - 1):
        tmp = ""
        if str2[i].isalpha() and str2[i + 1].isalpha():
            tmp += str2[i]
            tmp += str2[i + 1]
            str2_re.append(tmp)

    # 교집합
    if len(str1_re) > len(str2_re) :
        inter = [str1_re.remove(x) for x in str2_re if x in str1_re]
    else :
        inter = [str2_re.remove(x) for x in str1_re if x in str2_re]

    # 합집합
    union = str1_re + str2_re

    if len(union) == 0 :
        return 65536

    return int(len(inter) / len(union) * 65536)

if __name__ == '__main__' :
    str1_1 = "FRANCE"
    str2_1 = "french"

    str1_2 = "handshake"
    str2_2 = "shake hands"

    str1_3 = "aa1+aa2"
    str2_3 = "AAAA12"

    str1_4 = "E=M*C^2"
    str2_4 = "e=m*c^2"

    print(solution(str1_1, str2_1))
    print(solution(str1_2, str2_2))
    print(solution(str1_3, str2_3))
    print(solution(str1_4, str2_4))