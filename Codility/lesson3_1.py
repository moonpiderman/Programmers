def solution(x, y, d):
    chk = y - x
    if chk % d != 0:
        return (chk // d) + 1
    return chk // d


if __name__ == '__main__':
    print(solution(10, 85, 30))