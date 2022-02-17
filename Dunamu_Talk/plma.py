def solution(absolutes, sign):
    for i in range(len(sign)):
        if sign[i] == False:
            absolutes[i] *= -1

    return sum(absolutes)

if __name__ == '__main__':
    ab = [
        [4, 7, 12],
        [1, 2, 3]
    ]

    ss = [
        [True, False, True],
        [False, False, True]
    ]

    for i in range(len(ab)):
        print(solution(ab[i], ss[i]))
