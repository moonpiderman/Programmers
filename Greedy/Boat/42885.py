from itertools import combinations
from collections import deque
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
    answer = len(people)
    ppl = sorted(people, reverse=True)

    sp, ep = 0, len(ppl) - 1

    while sp < ep :
        if ppl[sp] + ppl[ep] <= limit :
            ep -= 1
            answer -= 1
        sp += 1

    return answer

def solution_mine(people, limit) :
    answer = 0
    people.sort()
    que = deque(people)

    while que :
        if len(que) >= 2 :
            if que[0] + que[-1] <= limit:
                que.pop()
                que.popleft()
                answer += 1
            elif que[0] + que[-1] > limit:
                que.pop()
                answer += 1
        else :
            if que[0] <= limit :
                que.pop()
                answer += 1


    return answer

if __name__ == '__main__' :
    people_1 = [70, 50, 80, 50]
    limit_1 = 100

    people_2 = [70, 80, 50]
    limit_2 = 100

    # print(solution(people_1, limit_1))
    # print(solution(people_2, limit_2))
    print(solution_mine(people_1, limit_1))
    print(solution_mine(people_2, limit_2))