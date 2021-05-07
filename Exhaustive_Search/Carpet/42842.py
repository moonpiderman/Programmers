def solution(brown, yellow):
    answer = []
    y_chk = []

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            y_chk.append(i)

    y_list = divisor(yellow)
    b_list = [[i[0] + 2, i[1] + 2] for i in y_list]

    if len(y_chk) % 2 == 1:
        for i in b_list:
            if i[0] == i[1]:
                answer.append(i[0])
                answer.append(i[1])
    elif len(y_chk) % 2 == 0:
        for i in b_list:
            if i[0] > i[1]:
                if (i[0] * i[1]) == (brown + yellow):
                    answer.append(i[0])
                    answer.append(i[1])
    return answer

def divisor(num) :
    div = []
    for i in range(1, num+1) :
        if num % i == 0 :
            div.append([i, num//i])
    return div

answer = []
brown = 8
yellow = 1

y_chk = []

for i in range(1, yellow+1) :
    if yellow % i == 0 :
        y_chk.append(i)

y_list = divisor(yellow)
b_list = [[i[0]+2, i[1]+2] for i in y_list]


if len(y_chk) % 2 == 1 :
    for i in b_list :
        if i[0] == i[1] :
            answer.append(i[0])
            answer.append(i[1])
elif len(y_chk) % 2 == 0 :
    for i in b_list :
        if i[0] > i[1] :
            if (i[0] * i[1]) == (brown + yellow) :
                answer.append(i[0])
                answer.append(i[1])

print(answer)