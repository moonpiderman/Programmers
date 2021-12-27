def solution(answers):
    answer = []
    check_1 = 0
    check_2 = 0
    check_3 = 0

    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if answers[i] == first[i % len(first)]:
            check_1 += 1
        if answers[i] == second[i % len(second)]:
            check_2 += 1
        if answers[i] == third[i % len(third)]:
            check_3 += 1

    resource = [check_1, check_2, check_3]

    for people, point in enumerate(resource):
        if point == max(resource):
            answer.append(people + 1)

    return answer

if __name__ == '__main__':
    answers = [
        [1, 2, 3, 4, 5],
        [1, 3, 2, 4, 2]
    ]

    for ans in answers:
        print(solution(ans))