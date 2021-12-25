def solution(n):
    answer = 0
    base_3 = ''
    tmp = ''
    base = [0, 1, 2]

    while n :
        base_3 = str(base[n % 3]) + base_3
        if n % 3 == 0 :
            n = (n // 3)
        else :
            n = n // 3
    base_3 = list(base_3)

    for i in range(len(base_3)) :
        answer += int(base_3[i]) * pow(3, i)

    return answer

if __name__ == '__main__' :
    n_1 = 45
    n_2 = 125

    print(solution(n_1))
    # print(solution(n_2))