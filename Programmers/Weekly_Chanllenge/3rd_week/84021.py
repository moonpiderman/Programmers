def solution(game_board, table):
    answer = -1



    return answer

if __name__ == '__main__':
    game_board_1 = [
        [1, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 0, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 0]
    ]

    table_1 = [
        [1, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1, 1],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 0]
    ]

    game_board_2 = [
        [0, 0, 0],
        [1, 1, 0],
        [1, 1, 1]
    ]

    table_2 = [
        [1, 1, 1],
        [1, 0, 0],
        [0, 0, 0]
    ]

    print(solution(game_board_1, table_1))
    # print(solution(game_board_2, table_2))