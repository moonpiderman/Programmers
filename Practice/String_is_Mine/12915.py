def solution(strings, n):
    answer = []

    for i in range(len(strings)) :
        strings[i] = strings[i][n] + strings[i]

    strings.sort()
    for i in range(len(strings)) :
        answer.append(strings[i][1:])

    return answer

if __name__ == '__main__' :
    strings_1 = ["sun", "bed", "car"]
    n_1 = 1
    strings_2 = ["abce", "abcd", "cdx"]
    n_2 = 2

    print(solution(strings_1, n_1))
    print(solution(strings_2, n_2))