from itertools import permutations
def solution(A):
    chk = list(permutations(A, 3))
    for c in chk:
        if c[0] + c[1] > c[2] and c[0] + c[2] > c[1] and c[1] + c[2] > c[0]:
            return 1
    return 0

if __name__ == '__main__':
    As = [
        [10, 2, 5, 1, 8, 20],
        [10, 50, 5, 1]
    ]
    for A in As:
        print(solution(A))