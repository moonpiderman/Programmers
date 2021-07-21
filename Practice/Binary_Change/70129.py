def counting(string, total_cnt, zero_cnt):
    total_c = total_cnt
    zero_c = zero_cnt
    s = string
    tmp = []

    for i in range(len(s)):
        if s[i] == '0':
            zero_c += 1
        elif s[i] == '1':
            tmp.append(s[i])

    # bin(integer) 함수 사용해서 binary 값으로 변경해주기

    total_c += 1
    return tmp, total_c, zero_c

def solution(s):
    answer = []
    total_cnt = 0
    zero_cnt = 0

    s = list(s)
    while s == '1':
        s, total_cnt, zero_cnt = counting(s, total_cnt, zero_cnt)

    print(s)
    print(total_cnt)
    print(zero_cnt)
    return answer

if __name__ == '__main__':
    s_1 = "110010101001"
    s_2 = "01110"
    s_3 = "1111111"

    print(solution(s_1))
    # print(solution(s_2))
    # print(solution(s_3))