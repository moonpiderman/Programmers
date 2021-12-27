from collections import deque
def solution(progresses, speeds):
    answer = []
    second = 0
    count = 0
    progresses = deque(progresses)
    speeds = deque(speeds)

    while len(speeds) > 0:
        if progresses[0] + (second * speeds[0]) >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            second += 1
    answer.append(count)
    return answer


if __name__ == '__main__':
    pro = [
        [93, 30, 55],
        [95, 90, 99, 99, 80, 99]
    ]
    spe = [
        [1, 30, 5],
        [1, 1, 1, 1, 1, 1]
    ]

    for i in range(len(pro)):
        print(solution(pro[i], spe[i]))