BOARD_SIZE = 8  # 체스판 크기를 8로 설정

board = [None] * BOARD_SIZE


def set_queen(row):
    global board
    for col in range(BOARD_SIZE):
        noset = False
        if row > 0:
            for i in range(row):
                dif = row - i
                if board[i] == col or board[i] == col + dif or board[i] == col - dif:
                    # 윗줄 수직 또는 대각선으로 이미 놓여있을 경우
                    noset = True
                    break
        if noset: continue
        board[row] = col
        if row + 1 >= BOARD_SIZE:
            # 마지막 줄까지 배치에 성공하였을 경우
            return True
        else:
            # 다음 줄 재귀호출
            if set_queen(row + 1): return True
            # 마지막 줄 배치 성공시 연쇄적으로 종료


if __name__ == "__main__":
    # 첫 줄부터 배치 시작
    if set_queen(0):
        for b in board:
            print("+---" * BOARD_SIZE + "+")
            for i in range(BOARD_SIZE):
                if b == i:
                    print("| Q ", end="")
                else:
                    print("|   ", end="")
            print("|")
        print("+---" * BOARD_SIZE + "+")