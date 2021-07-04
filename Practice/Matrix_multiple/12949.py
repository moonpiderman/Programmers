def solution(arr1, arr2):
    answer = []
    answer_row = len(arr1)
    answer_col = len(arr2[0])

    for i in range(answer_row) :
        tmp = []
        for j in range(answer_col) :
            result = 0
            for k in range(len(arr1[0])) :
                val1 = arr1[i][k]
                val2 = arr2[k][j]
                result += val1 * val2
            tmp.append(result)
        answer.append(tmp)

    return answer

if __name__ == '__main__' :
    arr1_1 = [[1, 4], [3, 2], [4, 1]]
    arr2_1 = [[3, 3], [3, 3]]

    arr1_2 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
    arr2_2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

    print(solution(arr1_1, arr2_1))
    print(solution(arr1_2, arr2_2))