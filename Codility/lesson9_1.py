def solution(A):
    mini = 200000
    max_profit = 0

    for i in range(1, len(A)):
        if mini > A[i - 1]:
            mini = A[i - 1]
        profit = max(0, A[i] - mini)
        max_profit = max(profit, max_profit)
    return max_profit

if __name__ == '__main__':
    A = [
        23171, 21011, 21123, 21366, 21367
    ]

    print(solution(A))