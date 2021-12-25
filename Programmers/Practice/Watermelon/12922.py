def solution(n):
    answer = ''

    for i in range(1, n + 1) :
        if i % 2 == 1 :
            answer += "수"
        elif i % 2 == 0 :
            answer += "박"

    return answer

if __name__ == '__main__' :
    n_1 = 3
    n_2 = 4

    print(solution(n_1))