from collections import deque


def solution(priorities, location):
    priorities = deque(priorities)
    queue = []

    for i in range(1, len(priorities)):
        if priorities[0] < priorities[i]:
            temp = priorities.popleft()
            queue.append(temp)
            break
        else:
            continue

    print(priorities)
    return priorities


# pri = [2, 1, 3, 2]
# loca = 2
pri = [1, 1, 9, 1, 1, 1]
loca = 0

solution(pri, loca)
