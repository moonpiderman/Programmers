def solution(A):
    if len(A) == 0:
        return None
    A = sorted(A)

    if A[0] != 1:
        return 0

    arr = [r for r in range(1, 1 + len(A))]

    for i in range(len(A)):
        if A[i] != arr[i]:
            return 0
    return 1

if __name__ == '__main__':
    A = [4, 1, 3, 2]
    print(solution(A))