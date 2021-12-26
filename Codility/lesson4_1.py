def solution(X, A):
    a = [0] * X
    result = 0

    for idx, val in enumerate(A):
        if a[val - 1] == 0:
            a[val - 1] = 1
            result += 1
        if result == X:
            return idx
    return -1

if __name__ == '__main__':
    X = 5
    A = [1, 3, 1, 4, 2, 3, 5, 4]

    print((solution(X, A)))