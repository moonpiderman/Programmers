def solution(clothes):
    answer = 1
    closet = {}

    for clo in clothes :
        type_cloth = clo[1]
        name_cloth = clo[0]
        if type_cloth in closet :
            closet[type_cloth].append(name_cloth)
        else :
            closet[type_cloth] = [name_cloth]

    for type_cloth in closet.keys() :
        answer = answer * (len(closet[type_cloth]) + 1)
    return answer - 1

clothes = [
    ["yellowhat", "headgear"],
    ["bluesunglasses", "eyewear"],
    ["green_turban", "headgear"]
]

answer = 1
closet = {}
for clo in clothes :
    type_cloth = clo[1]
    name_cloth = clo[0]
    if type_cloth in closet :
        closet[type_cloth].append(name_cloth)
    else :
        closet[type_cloth] = [name_cloth]

for type_cloth in closet.keys() :
    answer = answer * (len(closet[type_cloth]) + 1)

answer -= 1
print(answer)