def counting(string, total, zero):
    total_c = total
    zero_c = zero
    aws = string
    tmp = []


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

    return aws, total_c, zero_c

def solution(s):
    answer = []
    total_cnt = 0
    zero_cnt = 0

    while True:
        s, total_cnt, zero_cnt = counting(s, total_cnt, zero_cnt)
        if s == '1':
            break

    answer.append(total_cnt)
    answer.append(zero_cnt)

    return answer

if __name__ == '__main__':
    s_1 = "110010101001"
    s_2 = "01110"
    s_3 = "1111111"

    print(solution(s_1))
    print(solution(s_2))
    print(solution(s_3))