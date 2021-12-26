def solution(A, B, K):
    div_a, mod_a = divmod(A, K)
    div_b = B // K
    answer = div_b - div_a

    if mod_a == 0:
        answer += 1
    return answer

if __name__ == '__main__':
    print(solution(6, 11, 2))