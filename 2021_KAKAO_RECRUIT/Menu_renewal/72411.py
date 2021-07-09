from collections import Counter
from itertools import combinations

def solution_fail(orders, course):
    answer = []
    product = {}
    k = [] # key
    v = [] # value

    for i in range(len(orders)) :
        tmp = []
        for j in orders[i] :
            if j not in k :
                k.append(j)
                v.append(1)
            else :
                v[k.index(j)] += 1

    # k, v 에서 Key value 뽑아서 dictionary 만들기
    for i in range(len(k)) :
        product[k[i]] = v[i]

    print(product)
    ldict = sorted(product.items())
    print(ldict)

    return answer

def solution_fuckin_my_logic(orders, course) :
    answer = []
    stack = []
    orders.sort(key=len)
    print(orders)

    for i in range(len(orders)) :
        cnt = 1
        for j in range(i + 1, len(orders)) :
            # 문자열 그 자체가 순서대로 안에 들어있어야
            # 들어있는 것으로 인식한다.
            check = list(orders[i])
            target = list(orders[j])

            if check in target :
                cnt += 1
        if cnt >= 2 :
            stack.append(orders[i])

    # 추후에 course로 체크

    return answer

def solution(orders, course) :
    answer = []

    for c in course :
        tmp = []
        for order in orders :
            com = combinations(sorted(order), c)
            tmp += com
        odic = Counter(tmp)
        print (odic)

        if odic :
            m = max(list(odic.values()))
            if m >= 2 :
                for key, value in odic.items() :
                    if odic[key] == m :
                        answer.append(''.join(key))

    return sorted(answer)

if __name__ == '__main__' :
    orders_1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course_1 = [2, 3, 4]

    orders_2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
    course_2 = [2, 3, 5]

    orders_3 = ["XYZ", "XWY", "WXA"]
    course_3 = [2, 3, 4]

    # print(solution(orders_1, course_1))
    print(solution(orders_2, course_2))
    # print(solution(orders_3, course_3))