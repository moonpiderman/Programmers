def solution(A):
    length = len(A)
    chk_arr = [r for r in range(1, length + 1)]

    result = abs(sum(A) - sum(chk_arr))
    if result > 1000000000:
        return -1
    return result

if __name__ == '__main__':
    As = [
        [1, 2, 1],
        [2, 1, 4, 4],
        [6, 2, 3, 5, 6, 3]
    ]

    for A in As:
        print(solution(A))