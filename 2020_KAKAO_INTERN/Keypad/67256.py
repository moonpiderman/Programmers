def distance(target, left_loca, right_loca, hand) :
    left_dis = abs(target[0] - left_loca[0]) + abs(target[1] - left_loca[1])
    right_dis = abs(target[0] - right_loca[0]) + abs(target[1] - right_loca[1])

    if (left_dis == right_dis and hand == "left") or left_dis < right_dis :
        left_loca[0] = target[0]
        right_loca[1] = target[1]
        result = "L"
    else :
        left_loca[0] = target[0]
        right_loca[1] = target[1]
        result = "R"

    return left_loca, right_loca, result

def solution(numbers, hand):
    answer = ''
    handed = {"left": "L", "right": "R"}

    # keypad의 좌푯값
    keypad = {
        "1": [0, 0],
        "2": [0, 1],
        "3": [0, 2],
        "4": [1, 0],
        "5": [1, 1],
        "6": [1, 2],
        "7": [2, 0],
        "8": [2, 1],
        "9": [2, 2],
        "*": [3, 0],
        "0": [3, 1],
        "#": [3, 2]
    }
    # 첫 손가락의 위치
    left_loca = keypad["*"]
    right_loca = keypad["#"]

    for num in numbers :
        attack = keypad[str(num)]
        if num == 1 or num == 4 or num == 7 :
            left_loca[0] = attack[0]
            left_loca[1] = attack[1]
            pt = "L"
        elif num == 3 or num == 6 or num == 9 :
            right_loca[0] = attack[0]
            right_loca[1] = attack[1]
            pt = "R"
        else :
            left_loca, right_loca, pt = distance(attack, left_loca, right_loca, hand)

        answer = answer + pt

    return answer

if __name__ == '__main__' :
    numbers_1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand_1 = "right"

    numbers_2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand_2 = "left"

    numbers_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand_3 = "right"

    print(solution(numbers_1, hand_1))