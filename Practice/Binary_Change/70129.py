def counting(string):
    total_c = 0
    zero_c = 0
    aws = string
    tmp = []

    while aws != '1':
        aws = list(aws)
        for i in range(len(aws)):
            if aws[i] == '0':
                zero_c += 1
            elif aws[i] == '1':
                tmp.append(aws[i])

        length = len(tmp)
        binary = bin(length)
        aws = binary[2:]
        total_c += 1

    return total_c, zero_c

def solution(s):
    answer = []
    total_cnt, zero_cnt = counting(s)
    print(total_cnt)
    print(zero_cnt)

    # while s != '1':
    #     s, total_cnt, zero_cnt = counting(s, total_cnt, zero_cnt)

    return answer

if __name__ == '__main__':
    s_1 = "110010101001"
    s_2 = "01110"
    s_3 = "1111111"

    print(solution(s_1))
    # print(solution(s_2))
    # print(solution(s_3))