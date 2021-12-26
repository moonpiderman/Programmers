from collections import deque
def solution(A, K):
    if len(A) == 0:
        return []
    if len(set(A)) == 1:
        return A
    if len(A) == K:
        return A
    A = deque(A)

    while K > 0:
        out = A.pop()
        A.appendleft(out)
        K -= 1
    return list(A)

if __name__ == '__main__':
    As = [
        [3, 8, 9, 7, 6],
        [0, 0, 0],
        [1, 2, 3, 4]
    ]

    Ks = [
        3, 1, 4
    ]

    for i in range(len(As)):
        print(solution(As[i], Ks[i]))