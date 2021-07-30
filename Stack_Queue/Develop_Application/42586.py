def solution(progresses, speeds):
    return_value = []
    second = 0
    count = 0
    while len(speeds) > 0:
        if progresses[0] + (second * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                return_value.append(count)
                count = 0
            second += 1
    return_value.append(count)
    return return_value

if __name__ == '__main__':
    progresses_1 = [93, 30, 55]
    speeds_1 = [1, 30, 5]

    progresses_2 = [95, 90, 99, 99, 80, 99]
    speeds_2 = [1, 1, 1, 1, 1, 1]

    print(solution(progresses_1, speeds_1))
    print(solution(progresses_2, speeds_2))