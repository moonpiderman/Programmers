def solution(phone_number):
    phone_number = list(phone_number)
    for i in range(len(phone_number) - 4):
        phone_number[i] = '*'
    return "".join(phone_number)

if __name__ == '__main__':
    pn = "01033334444"
    pn2 = "027778888"
    print(solution(pn))
    print(solution(pn2))

