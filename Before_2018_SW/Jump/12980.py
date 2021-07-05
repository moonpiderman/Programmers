def solution(n):
    answer = 0

    while n > 0 :
        div, mod = divmod(n, 2)
        n = div
        if mod != 0 :
            answer += 1
    return answer

if __name__ == '__main__' :
    n_1 = 5
    n_2 = 6
    n_3 = 5000

    print(solution(n_1))
    print(solution(n_2))
    print(solution(n_3))