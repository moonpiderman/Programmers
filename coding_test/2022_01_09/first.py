def cal_celcius(temp):
    return 20 - abs(22 - temp)

def sky_status(status):
    if status == 1 or status == 2:
        return 20
    elif status == 3:
        return 17
    elif status == 4:
        return 10

def rainy_status(status):
    if status == 0:
        return 0
    elif status == 1:
        return 5
    elif status == 2:
        return 14

def chk_worst(dictionary, idx):
    if dictionary[idx][0] == 4 or dictionary[idx][1] == 1 or (0 >= dictionary[idx][2] >= 30):
        return True
    return False

def solution(data):
    answer = []
    best_day = [5, 4, 6, 2, 3, 1, 0]
    dic = {}
    chk = []
    for i, d in enumerate(data):
        result = sky_status(d[0]) + rainy_status(d[1]) + cal_celcius(d[2])
        chk.append(result)
        dic[i] = d

    maxi = max(chk)

    maxi_day = []
    for key, value in dic.items():
        if value[1] == maxi:
            maxi_day.append(key)

    if len(maxi_day) == 1:
        answer.append(maxi_day[0])
    # else: 베스트 데이 체크

    if chk_worst(dic, chk.index(min(chk))) is False:
        answer.append(-1)
    # else:


    # worst = chk_worst(dic, result.index(min(result)))


    return answer

if __name__ == '__main__':
    first = [
        [1, 0, 11], [3, 1, 15], [2, 0, 16], [4, 0, 17], [2, 0, 15], [2, 1, 14], [2, 0, 12]
    ]
    second = [
        [4, 0, 12], [1, 0, 16], [3, 0, 18], [3, 0, 17], [2, 0, 15], [3, 2, 22], [2, 1, 17]
    ]

    print(solution(first))
    print(solution(second))