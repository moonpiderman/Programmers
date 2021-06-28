def solution(a, b):
    answer = 0
    length = len(a)

    for i in range(length) :
        answer += (a[i] * b[i])

    return answer

if __name__ == '__main__' :
    a_1 = [1, 2, 3, 4]
    b_1 = [-3, -1, 0, 2]

    a_2 = [-1, 0, 1]
    b_2 = [1, 0, -1]

    print(solution(a_1, b_1))
    print(solution(a_2, b_2))