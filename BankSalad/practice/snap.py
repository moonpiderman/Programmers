def solution(ex):
    sorted_ex = sorted(ex, key=lambda x: x[0])
    result = []

    for range in sorted_ex:
        if result and range[0] <= result[-1][1]:
            result[-1] = (result[-1][0], max(range[1], result[-1][1]))
        else:
            result.append(range)

    return result

def merge(arr):
    sorted_arr = sorted(arr, key=lambda x: x[0])
    result = []

    for ex in sorted_arr:
        if result and result[-1][1] >= ex[0]:
            result[-1] = (result[-1][0], max(result[-1][1], ex[1]))
        else:
            result.append(ex)

    return result


if __name__ == '__main__':
    example = [
        (1, 3), (5, 8), (4, 10), (20, 25)
    ]
    print(example)
    print(solution(example))
    print(merge(example))