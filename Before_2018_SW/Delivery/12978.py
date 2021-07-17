def solution(N, road, K):
    answer = 0
    for i in road:
        if i[0] > i[1]:
            tmp = i[0]
            i[0] = i[1]
            i[1] = tmp



    return answer

if __name__ == '__main__':
    N_1 = 5
    road_1 = [
        [1, 2, 1],
        [2, 3, 3],
        [5, 2, 2],
        [1, 4, 2],
        [5, 3, 1],
        [5, 4, 2]
    ]
    K_1 = 3

    N_2 = 6
    road_2 = [
        [1, 2, 1],
        [1, 3, 2],
        [2, 3, 2],
        [3, 4, 3],
        [3, 5, 2],
        [3, 5, 3],
        [5, 6, 1]
    ]
    K_2 = 4

    print(solution(N_1, road_1, K_1))
    # print(solution(N_2, road_2, K_2))