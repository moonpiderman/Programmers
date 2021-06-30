import math

def distance_check(l_loca, r_loca, target, hand):
    left = l_loca
    right = r_loca
    l_distance = math.sqrt(pow(abs(target[0] - left[0]), 2) + pow(abs(target[1] - left[1]), 2))
    r_distance = math.sqrt(pow(abs(target[0] - right[0]), 2) + pow(abs(target[1] - right[1]), 2))

    if l_distance == r_distance :
        if hand == "left" :
            finger = "L"
            left = target
        elif hand == "right" :
            finger = "R"
            right = target

    elif l_distance > r_distance :
        finger = "R"
        right = target

    elif r_distance > l_distance :
        finger = "L"
        left = target

    return left, right, finger

def solution(numbers, hand):
    answer = ''
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
    # 초기 위치설정
    l_loca = keypad["*"]
    r_loca = keypad["#"]

    print("첫 위치 :", l_loca, r_loca)

    for num in numbers :
        target = keypad[str(num)]
        if num == 1 or num == 4 or num == 7 :
            l_loca[0] = target[0]
            l_loca[1] = target[1]
            finger = "L"
        elif num == 3 or num == 6 or num == 9 :
            r_loca[0] = target[0]
            r_loca[1] = target[1]
            finger = "R"
        else :
            l_loca, r_loca, finger = distance_check(l_loca, r_loca, target, hand)

        answer += finger
        print(l_loca, r_loca)
    return answer

if __name__ == '__main__' :
    numbers_1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    hand_1 = "right"

    numbers_2 = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
    hand_2 = "left"

    numbers_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    hand_3 = "right"

    # print(solution(numbers_1, hand_1))
    print(solution(numbers_2, hand_2))
    # print(solution(numbers_3, hand_3))