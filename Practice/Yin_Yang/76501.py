def solution(absolutes, signs):
    answer = 0

    for i in range(len(signs)) :
        if signs[i] == False :
            absolutes[i] *= -1

    answer = sum(absolutes)

    return answer

if __name__ == '__main__' :
    absolutes_1 = [4, 7, 12]
    signs_1 = [True, False, True]

    absolutes_2 = [1, 2, 3]
    signs_2 = [False, False, True]

    print(solution(absolutes_1, signs_1))