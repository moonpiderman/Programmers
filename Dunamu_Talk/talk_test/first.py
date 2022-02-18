def solution(a, b, budget):
    answer = 0

    max_a = budget // a
    max_b = budget // b

    for cnt_a in range(max_a + 1):
        for cnt_b in range(max_b + 1):
            if (cnt_a * a) + (cnt_b * b) == budget:
                answer += 1

    return answer

if __name__ == '__main__':
    a = 3000
    b = 5000
    budget = 23000

    print(solution(a, b, budget))