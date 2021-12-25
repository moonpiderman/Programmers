def solution(s):
    answer = ''
    array = s.split(' ')

    for i in range(len(array)) :
        array[i] = int(array[i])

    answer += str(min(array)) + ' '
    answer += str(max(array))

    return answer

if __name__ == '__main__' :
    s_1 = "1 2 3 4"
    s_2 = "-1 -2 -3 -4"
    s_3 = '-1 -1'

    print(solution(s_1))
    # print(solution(s_2))
    # print(solution(s_3))