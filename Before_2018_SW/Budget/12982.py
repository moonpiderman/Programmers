def solution(d, budget):
    answer = 0
    result = 0
    d = sorted(d)

    for i in d :
        result += i
        if result <= budget :
            answer += 1
            continue
        else :
            break

    return answer

if __name__ == '__main__' :
    d_1 = [1, 3, 2, 5, 4]
    budget_1 = 9
    d_2 = [2, 2, 2, 3]
    budget_2 = 10

    print(solution(d_1, budget_1))
    # print(solution(d_2, budget_2))