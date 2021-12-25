def solution(lottos, win_nums):
    answer = [0, 0]
    score = [6, 6, 5, 4, 3, 2, 1]

    cnt = 0
    zero_cnt = lottos.count(0)

    for num in lottos :
        if num in win_nums :
            cnt += 1

    answer[0], answer[1] = score[cnt + zero_cnt], score[cnt]

    return answer

if __name__ == '__main__' :
    lottos_1 = [44, 1, 0, 0, 31, 25]
    win_nums_1 = [31, 10, 45, 1, 6, 19]

    lottos_2 = [0, 0, 0, 0, 0, 0]
    win_nums_2 = [38, 19, 20, 40, 15, 25]

    lottos_3 = [45, 4, 35, 20, 3, 9]
    win_nums_3 = [20, 9, 3, 45, 4, 35]

    print(solution(lottos_1, win_nums_1))
    print(solution(lottos_2, win_nums_2))
    print(solution(lottos_3, win_nums_3))