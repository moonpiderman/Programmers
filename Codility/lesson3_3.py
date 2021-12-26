def solution(A):
    sum_1 = 0
    sum_2 = sum(A)
    mini = None

    for i in range(1, len(A)):
        sum_1 += A[i - 1]
        sum_2 -= A[i - 1]
        tmp = abs(sum_1 - sum_2)

        if mini == None:
            mini = tmp
        else:
            mini = min(mini, tmp)

    return mini

if __name__ == '__main__':
    A = [3, 1, 2, 4, 3]
    print((solution(A)))