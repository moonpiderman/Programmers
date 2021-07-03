from collections import deque

def solution(board, moves):
    answer = 0
    stack = [] # 쌓을 곳

    for i in range(len(board)) :
        board[i] = deque(board[i])


    return answer

if __name__ == '__main__' :
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]

    print(solution(board, moves))