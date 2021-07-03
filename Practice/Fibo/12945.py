def fibo(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    elif n >= 2 :
        return fibo(n-1) + fibo(n-2)

def solution(n):
    answer = fibo(n)
    answer %= 1234567
    return answer

if __name__ == '__main__' :
    n_1 = 3
    n_2 = 5

    print(solution(n_1))
    print(solution(n_2))