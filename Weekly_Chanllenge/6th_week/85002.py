def solution(weights, head2head):
    field = []

    # winning rate
    for i in range(len(weights)):
        fight_cnt = 0
        w_cnt = 0
        heavy_cnt = 0
        for j in range(len(weights)):
            if head2head[i][j] != 'N':
                fight_cnt += 1
                if head2head[i][j] == 'W':
                    w_cnt += 1
                    if weights[i] < weights[j]:
                        heavy_cnt += 1
        if fight_cnt == 0:
            w_rate = 0
        else:
            w_rate = w_cnt / fight_cnt
        # i_player = ( i + 1, weight[i], winning_rate, up_cnt )
        i_player = (i + 1, weights[i], w_rate, heavy_cnt)
        field.append(i_player)

    sorted_field = sorted(field, key=lambda x: (-x[2], -x[3], -x[1], x[0]))

    answer = [x[0] for x in sorted_field]

    return answer

if __name__ == '__main__':
    weights_1 = [50, 82, 75, 120]
    head2head_1 = ["NLWL", "WNLL", "LWNW", "WWLN"]

    weights_2 = [145, 92, 86]
    head2head_2 = ["NLW", "WNL", "LWN"]

    weights_3 = [60, 70, 60]
    head2head_3 = ["NNN", "NNN", "NNN"]

    print(solution(weights_1, head2head_1))
    print(solution(weights_2, head2head_2))
    print(solution(weights_3, head2head_3))