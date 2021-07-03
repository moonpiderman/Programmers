from itertools import combinations
def solution_fail(people, limit):
    answer = 0
    com = list(combinations(people, 2))

    for i in range(len(com)) :
        if com[i][0] + com[i][1] <= limit :
            people.remove(com[i][0])
            people.remove(com[i][1])
            answer += 1

    answer += len(people)

    return answer

def solution(people, limit) :
    answer = 0
    return answer

if __name__ == '__main__' :
    people_1 = [70, 50, 80, 50]
    limit_1 = 100

    people_2 = [70, 80, 50]
    limit_2 = 100

    print(solution(people_1, limit_1))
    print(solution(people_2, limit_2))