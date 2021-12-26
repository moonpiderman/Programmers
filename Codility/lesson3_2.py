def solution(A):
    summ = 0
    for val in range(1, len(A) + 2):
        summ += val
    return summ - sum(A)

if __name__ == '__main__':
    A = [2, 3, 1, 5]
    print(solution(A))