from collections import deque
def solution(priorities, location):
    answer = 0
    deq = deque()
    for i, v in enumerate(priorities):
        t = [i, v]
        deq.append(t)

    while deq:
        pop = deq.popleft()
        if deq and max(deq)[0] > pop[0]:
            deq.append(pop)
        else:
            answer += 1
            if pop[1] == location:
                break
    return answer

if __name__ == '__main__':
    pr = [
        [2, 1, 3, 2],
        [1, 1, 9, 1, 1, 1]
    ]

    lo = [
        2, 0
    ]

    for i in range(len(pr)):
        print(solution(pr[i], lo[i]))