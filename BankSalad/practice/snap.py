def solution(ex):
    sorted_ex = sorted(ex, key=lambda x: x[0])
    result = []

    for range in sorted_ex:
        if result and range[0] <= result[-1][1]:
            result[-1] = (result[-1][0], max(range[1], result[-1][1]))
        else:
            result.append(range)

    return result

if __name__ == '__main__':
    example = [
        (1, 3), (5, 8), (4, 10), (20, 25)
    ]
    print(example)
    print(solution(example))