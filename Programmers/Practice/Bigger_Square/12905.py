def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])

    for r in board :
        if sum(r) :
            answer = 1
            break
    else :
        return 0

    for i in range(1, row) :
        for j in range(1, col) :
            if board[i - 1][j - 1] and board[i - 1][j] and board[i][j - 1] and board[i][j] :
                mini = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1
                board[i][j] = mini
                answer = max(answer, board[i][j])

    return answer ** 2

if __name__ == '__main__' :
    board_1 = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 1, 0]
    ]

    board_2 = [
        [0, 0, 1, 1],
        [1, 1, 1, 1]
    ]

    print(solution(board_1))
    # print(solution(board_2))