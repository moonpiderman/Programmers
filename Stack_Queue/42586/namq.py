from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while progresses:

        cnt = 0

        # 올림 사용하기
        p = (100 - progresses[0]) / speeds[0]
        mod = (100 - progresses[0]) % speeds[0]
        if mod > 0:
            p = math.ceil(p)

        for i in range(len(progresses)):
            progresses[i] += (p * speeds[i])

        while progresses[0] >= 100:
            cnt += 1

            progresses.popleft()
            speeds.popleft()

            if not progresses:
                break
        answer.append(cnt)
    return answer
