def manhatten(p1, p2):
    res = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    return res


def queen(board):
    new_board = [r for r in board]
    ppl = []
    man = []

    for i in range(5):
        for j in range(5):
            if new_board[i][j] == 'P':
                ppl.append([i, j])

    for i in range(len(ppl)):
        for j in range(i + 1, len(ppl)):
            man.append([manhatten(ppl[i], ppl[j]), ppl[i], ppl[j]])

    for chk in man:
        if chk[0] == 0:
            continue
        elif chk[0] == 1:
            really = 0
            return really
        elif chk[0] == 2:
            if new_board[chk[1][0]][chk[2][1]] == 'O' or new_board[chk[2][0]][chk[1][1]] == 'O':
                really = 0
                return really
    really = 1
    return really


def solution(places):
    result = []
    for wait in places:
        result.append(queen(wait))
    return result

places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]

result = []
for wait in places :
    result.append(queen(wait))

print(result)