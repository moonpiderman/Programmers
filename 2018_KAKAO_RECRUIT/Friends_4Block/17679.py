def solution(m, n, board):
    answer = 0
    col = n
    row = m
    # board 쪼개기
    for i in range(len(board)) :
        board[i] = list(board[i])

    while True :
        remove = [[0 for i in range(col)] for _ in range(row)]
        for r in range(row - 1) :
            for c in range(col - 1) :
                if board[r][c] != 0 and board[r][c] == board[r][c + 1] and board[r][c] == board[r + 1][c] and board[r][c] == board[r + 1][c + 1] :
                    remove[r][c], remove[r + 1][c], remove[r][c + 1], remove[r + 1][c + 1] = 1, 1, 1, 1

        cnt = 0
        for k in range(row) :
            cnt += sum(remove[k])
        answer += cnt
        if cnt == 0 :
            break
        for i in range(row - 1, -1, -1) :
            for j in range(col) :
                if remove[i][j] == 1:
                    x = i - 1
                    while x >= 0 and remove[x][j] == 1:
                        x -= 1
                    if x < 0 :
                        board[i][j] = 0
                    else :
                        board[i][j] = board[x][j]
                        remove[x][j] = 1

    return answer

if __name__ == '__main__' :
    m_1 = 4
    n_1 = 5
    board_1 = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

    m_2 = 6
    n_2 = 6
    board_2 = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

    # print(solution(m_1, n_1, board_1))
    print(solution(m_2, n_2, board_2))