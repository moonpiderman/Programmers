def difference(pro, spd):
    result = 100 - pro
    div = result // spd
    mod = result % spd

    if mod > 0:
        div += 1
    return div


def make_diff_arr(progresses, speeds):
    made_arr = []
    for i in range(len(speeds)):
        made_arr.append(difference(progresses[i], speeds[i]))
    return made_arr


def solution(progresses, speeds):
    diff = make_diff_arr(progresses, speeds)
    print(diff)
    return_value = []
    count = 1
    stack = [0]
    for i in range(1, len(diff)):
        while stack:
            index = stack[-1]
            if diff[index] > diff[i]:
                count += 1
                stack.pop()
            else:
                return_value.append(count)
                stack.pop()
                count = 1
                continue
        stack.append(i)
    print(return_value)
    return return_value


p = [95, 90, 99, 99, 80, 99]
s = [1, 1, 1, 1, 1]

solution(p, s)
