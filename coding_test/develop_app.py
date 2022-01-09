from collections import deque
def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    count = 0
    second = 0
    answer = []

    while speeds:
        if (progresses[0] + (second * speeds[0])) >= 100:
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
    progresses = [
        [93, 30, 55],
        [95, 90, 99, 99, 80, 99]
    ]

    speeds = [
        [1, 30, 5],
        [1, 1, 1, 1, 1, 1]
    ]

    for i in range(len(progresses)):
        print("sol ", end="")
        print(i + 1, end=": ")
        print(solution(progresses[i], speeds[i]))
