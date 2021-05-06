from collections import deque


def solution_fail(priorities, location):
    answer = 0
    val_location = priorities[location]

    pop_idx = 0
    pop_pri = 0

    # 인덱스 deque 생성
    index = []
    for i in range(len(priorities)):
        index.append(i)
    index = deque(index)

    # deque of priorities
    p = deque(priorities)

    for i in range(len(priorities)):
        for j in range(i + 1, len(priorities)):
            if priorities[i] < priorities[j]:
                pop_idx = index.popleft()
                pop_pri = p.popleft()
                index.append(pop_idx)
                p.append(pop_pri)
                break

    p = list(p)
    index = list(index)

    for i in range(len(priorities)):
        if index[i] == location and p[i] == val_location:
            answer = i + 1

    return answer


def solution(priorities, location):
    answer = 0
    p = deque([(v, i) for i, v in enumerate(priorities)])

    while len(p):
        val = p.popleft()
        if p and max(p)[0] > val[0]:
            p.append(val)
        else:
            answer += 1
            if val[1] == location:
                break
    return answer


priorities = [2, 1, 3, 2]
location = 2

# priorities = [1, 1, 9, 1, 1, 1]
# location = 0

answer = 0

d = deque([(v, i) for i, v in enumerate(priorities)])

while len(d):
    val = d.popleft()
    print(val)
    if d and max(d)[0] > val[0]:
        d.append(val)
    else:
        answer += 1
        if val[1] == location:
            break
print(answer)
