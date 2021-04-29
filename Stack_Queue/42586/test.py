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


p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1, 1]

a = solution(p, s)
print(a)
