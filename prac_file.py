import sys


def memoization_fibo(n) :
    memo[0] = 1
    memo[1] = 1

    if n < 2 :
        return memo[n]

    for i in range(2, n + 1) :
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[n]

def fibo_bottom_up(n) :
    if n <= 1:
        return n

    fir = 0
    sec = 1
    for i in range(0, n - 1) :
        next = fir + sec
        fir = sec
        sec = next
    return next

def fibo_top_down(n) :
    if memo[n] > 0 :
        return memo[n]

    if n <= 1:
        memo[n] = n
        return memo[n]

    else :
        memo[n] = fibo_top_down(n - 1) + fibo_top_down(n - 2)
        return memo[n]

if __name__ == '__main__' :
    n = int(sys.stdin.readline())
    memo = [ 0 for i in range(n + 2) ]

    for i in range(n + 1) :
        print(memoization_fibo(i), end=' ')