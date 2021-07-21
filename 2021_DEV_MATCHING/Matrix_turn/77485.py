def turning(query, frame):
    turned_num = []
    top, left, bottom, right = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1

    tmp = frame[top][left]
    for y in range(top, bottom):
        frame[y][left] = frame[y + 1][left]
        turned_num.append(frame[y][left])

    for x in range(left, right):
        frame[bottom][x] = frame[bottom][x + 1]
        turned_num.append(frame[bottom][x])

    for y in range(bottom, top, -1):
        frame[y][right] = frame[y - 1][right]
        turned_num.append(frame[y][right])

    for x in range(right, left, -1):
        frame[top][x] = frame[top][x - 1]
        turned_num.append(frame[top][x])

    turned_num.append(tmp)
    frame[top][left + 1] = tmp

    return frame, min(turned_num)

def solution(rows, columns, queries):
    answer = []

    # 틀 형성
    frame = []
    for i in range(1, rows + 1):
        tmp = []
        for j in range(1, columns + 1):
            num = ((i - 1) * columns + j)
            tmp.append(num)
        frame.append(tmp)

    # 실행을 위한 구문
    for query in queries:
        frame, minimum = turning(query, frame)
        answer.append(minimum)

    return answer

if __name__ == '__main__':
    rows_1 = 6
    columns_1 = 6
    queries_1 = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]

    rows_2 = 3
    columns_2 = 3
    queries_2 = [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]

    rows_3 = 100
    columns_3 = 97
    queries_3 = [[1, 1, 100, 97]]

    print(solution(rows_1, columns_1, queries_1))
    print(solution(rows_2, columns_2, queries_2))
    print(solution(rows_3, columns_3, queries_3))