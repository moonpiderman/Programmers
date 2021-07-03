def fibo_recursive(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    elif n >= 2 :
        return fibo_recursive(n-1) + fibo_recursive(n-2)

def fibo(n) :
    if n < 2 :
        return n
    a, b = 0, 1
    for i in range(n - 1) :
        a, b = b, a + b

    return b

def solution(n):
    answer = fibo(n)
    answer %= 1234567
    return answer

if __name__ == '__main__' :
    n_1 = 3
    n_2 = 5

    print(solution(n_1))
    print(solution(n_2))