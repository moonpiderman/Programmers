def solution_fail(dirs):
    answer = 0
    sp = [0, 0]
    point = []
    u, d, l, r = [0, 1], [0, -1], [-1, 0], [1, 0]
    road = []

    point.append([0, 0])
    for cmd in dirs :
        tmp = []
        # 여기에 x > 5, x < -5, y > 5, y < -5 요건 추가
        if cmd == 'U' :
            sp[0] += u[0]
            sp[1] += u[1]
            tmp.append(sp[0])
            tmp.append(sp[1])

        elif cmd == 'D' :
            sp[0] += d[0]
            sp[1] += d[1]
            tmp.append(sp[0])
            tmp.append(sp[1])

        elif cmd == 'L' :
            sp[0] += l[0]
            sp[1] += l[1]
            tmp.append(sp[0])
            tmp.append(sp[1])

        elif cmd == 'R' :
            sp[0] += r[0]
            sp[1] += r[1]
            tmp.append(sp[0])
            tmp.append(sp[1])

        point.append(tmp)

    print(point)

    # 길 루틴
    for i in range(len(point) - 1) :
        tmp = []
        tmp.append(point[i])
        tmp.append(point[i + 1])
        if tmp not in road :
            road.append(tmp)
        else :
            continue

    print(road)

    return answer

def solution(dirs) :
    cmd = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0)
    }
    road = set()
    cur_x, cur_y = (0, 0)

    for rou in dirs :
        next_x, next_y = cur_x + cmd[rou][0], cur_y + cmd[rou][1]
        if -5 <= next_x <= 5 and -5 <= next_y <= 5 :
            road.add((cur_x, cur_y, next_x, next_y))
            road.add((next_x, next_y, cur_x, cur_y))
            cur_x, cur_y = next_x, next_y

    return len(road) // 2

if __name__ == '__main__' :
    dirs_1 = "ULURRDLLU"
    dirs_2 = "LULLLLLLU"

    # print(solution(dirs_1))
    print(solution(dirs_2))