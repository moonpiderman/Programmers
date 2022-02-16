def solution(clothes):


    return True

if __name__ == '__main__':
    clothes_1 = [
        ["yellowhat", "headgear"],
        ["bluesunglasses", "eyewear"],
        ["green_turban", "headgear"]
    ]

    clothes_2 = [
        ["crowmask", "face"],
        ["bluesunglasses", "face"],
        ["smoky_makeup", "face"]
    ]

    print(solution(clothes_1))
    print(solution(clothes_2))
