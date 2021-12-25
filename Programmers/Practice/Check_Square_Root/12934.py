import math

def solution(n):
    n = math.sqrt(n)

    if n % 1 != 0 :
        answer = -1
    else :
        n += 1
        answer = int(math.pow(n, 2))
    return answer

if __name__ == '__main__' :
    n_1 = 121
    n_2 = 3

    print(solution(n_1))