def solution(estimates, k):
    answer = 0

    for i in range(len(estimates) - k + 1):
        tmp = sum(estimates[i:i + k]) # 원흉
        if tmp > answer:
            answer = tmp

    return answer

if __name__ == '__main__':
    estimates = [
        [5, 1, 9, 8, 10, 5],
        [10, 1, 10, 1, 1, 4, 3, 10]
    ]

    ks = [3, 6]

    for i in range(len(ks)):
        print(solution(estimates[i], ks[i]))
