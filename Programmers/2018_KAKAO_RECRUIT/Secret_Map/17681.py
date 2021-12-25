def solution(n, arr1, arr2):
    answer = [ "" for r in range(n) ]
    lst_1 = []
    lst_2 = []

    for i in range(n) :
        res1 = '{0:b}'.format(arr1[i]).zfill(n)
        res2 = '{0:b}'.format(arr2[i]).zfill(n)
        lst_1.append(res1)
        lst_2.append(res2)

    for i in range(n) :
        for j in range(n) :
            if lst_1[i][j] == '0' and lst_2[i][j] == '0' :
                answer[i] += " "
            else :
                answer[i] += "#"

    return answer

if __name__ == '__main__' :
    n_1 = 5
    arr1_1 = [9, 20, 28, 18, 11]
    arr2_1 = [30, 1, 21, 17, 28]

    n_2 = 6
    arr1_2 = [46, 33, 33 ,22, 31, 50]
    arr2_2 = [27 ,56, 19, 14, 14, 10]

    # print(solution(n_1, arr1_1, arr2_1))
    print(solution(n_2, arr1_2, arr2_2))