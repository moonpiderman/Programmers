def solution(arr):
    answer = 0
    arr = sorted(arr, reverse=True)

    for i in range(len(arr) - 1) :
        for j in range(arr[i], (arr[i] * arr[i + 1]) + 1) :
            if j % arr[i] == 0 and j % arr[i + 1] == 0 :
                break
        arr[i + 1] = j

    answer = arr[-1]

    return answer

if __name__ == '__main__' :
    arr_1 = [2, 6, 8, 14]
    arr_2 = [1, 2, 3]

    print(solution(arr_1))
    print(solution(arr_2))