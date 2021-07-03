from collections import deque

def solution_fail(board, moves):
    answer = 0
    drop = [] # 쌓을 곳
    drop = deque(drop)
    temper = [ [] for r in range(len(board)) ]
    temper = deque(temper)

    # 열별로 뒤집고 deque
    for i in range(len(board)) :
        for j in range(len(board)) :
            if board[j][i] != 0 :
                temper[i].append(board[j][i])
        temper[i] = deque(temper[i])

    for pop in range(len(moves)) :
        idx = moves[pop] - 1
        if len(temper[idx]) == 0:
            continue
        else :
            if len(drop) == 0:
                drop.append(temper[idx].popleft())
            else :
                dpop = drop.pop()
                if temper[idx][0] == dpop:
                    answer += 2
                else :
                    drop.append(dpop)
                    drop.append(temper[idx].popleft())


    return answer

def solution(board, moves) :
    answer = 0



    return answer

if __name__ == '__main__' :
    board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
    moves = [1, 5, 3, 5, 1, 2, 1, 4]

    print(solution(board, moves))