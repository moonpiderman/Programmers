def solution(A, B):
    answer = 0

    A = sorted(A)
    B = sorted(B, reverse=True)

    for i in range(len(A)) :
        answer += (A[i] * B[i])

    return answer

if __name__ == '__main__' :
    A_1 = [1, 4, 2]
    B_1 = [5, 4, 4]

    A_2 = [1, 2]
    B_2 = [3, 4]

    print(solution(A_1, B_1))
    # print(solution(A_2, B_2))