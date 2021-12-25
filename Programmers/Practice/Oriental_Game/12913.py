def solution_fail(land):
    answer = 0
    row = len(land)

    for i in range(row) :
        for j in range(4) :
            if i == 0 :
                if max(land[i]) == land[i][j] :
                    stop = j
                    break
            else :
                land[i][stop] = 0
                if max(land[i]) == land[i][j] :
                    stop = j
                    break
        answer += max(land[i])
    return answer

def solution(land) :
    n = len(land) - 1
    for i in range(n) :
        land[i + 1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i + 1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i + 1][2] += max(land[i][0], land[i][1], land[i][3])
        land[i + 1][3] += max(land[i][0], land[i][1], land[i][2])
    return max(land[n])

if __name__ == '__main__' :
    land = [[1, 2, 3, 5],
            [5, 6, 7, 8],
            [4, 3, 2, 1]]

    print(solution(land))