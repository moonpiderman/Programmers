def quater(array, r_s, r_e, c_s, c_e):
    quat = []
    half = len(array) // 2
    all = len(array)
    for i in range(r_s, r_e):
        tmp = []
        for j in range(c_s, c_e):
            tmp.append(array[i][j])
        quat.append(tmp)
    return quat

def solution_fail(arr):
    answer = []
    distance = len(arr)

    while distance > 2:
        half = distance // 2
        first_quat = quater(arr, 0, half, 0, half)
        second_quat = quater(arr, 0, half, half, distance)
        third_quat = quater(arr, half, distance, 0, half)
        fourth_quat = quater(arr, half, distance, half, distance)

        # 잘라낸 내부에서 0, 1 체크?
        distance = half
    return answer

def solution(arr):
    answer = [0, 0]
    N = len(arr)

    def comp(x, y, n):
        chk = arr[x][y]
        for i in range(x, x + n):
            for j in range(y, y + n):
                if arr[i][j] != chk:
                    nn = n // 2
                    comp(x, y, nn)
                    comp(x + nn, y, nn)
                    comp(x, y + nn, nn)
                    comp(x + nn, y + nn, nn)
                    return

        answer[chk] += 1
    comp(0, 0, N)
    return answer

if __name__ == '__main__':
    arr_1 = [
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 1]
    ]
    arr_2 = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 1, 1, 1, 1],
        [0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1],
        [0, 0, 0, 0, 1, 1, 1, 1]
    ]

    print(solution(arr_1))
    print(solution(arr_2))