def solution(arr1, arr2):
    answer = []
    row = len(arr1)
    col = len(arr1[0])

    for r in range(row) :
        tmp = []
        for c in range(col) :
            result = arr1[r][c] + arr2[r][c]
            tmp.append(result)
        answer.append(tmp)

    return answer

if __name__ == '__main__' :
    arr1_1 = [[1, 2], [2, 3]]
    arr2_1 = [[3, 4], [5, 6]]

    arr1_2 = [[1], [2]]
    arr2_2 = [[3], [4]]

    print(solution(arr1_1, arr2_1))
    # print(solution(arr1_2, arr2_2))