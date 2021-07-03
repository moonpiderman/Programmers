def solution(n):
    answer = 0

    for i in range(1, n + 1) :
        chk = 0
        for j in range(i, n + 1) :
            chk += j
            if chk < n :
                continue
            elif chk == n :
                answer += 1
                break
            else :
                break

    return answer

if __name__ == '__main__' :
    n = 15
    print(solution(n))