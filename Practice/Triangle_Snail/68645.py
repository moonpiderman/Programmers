def counting(num) :
    mul = 0
    if num == 0:
        return 0
    elif num == 1 :
        mul = 1
    elif num > 1 :
        mul = num * num

    return mul - counting(num - 1)

def solution_fail(n):
    answer = []
    count = counting(n)
    chk = [ k for k in range(1, count + 1) ]

    return answer

def solution(n) :
    answer = [ [ 0 for k in range(1, i + 1) ] for i in range(1, n + 1) ]

    x, y = -1, 0
    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    return sum(answer, [])

if __name__ == '__main__' :
    n_1 = 4
    n_2 = 5
    n_3 = 6

    print(solution(n_1))
    # print(solution(n_2))
    # print(solution(n_3))