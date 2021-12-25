def yaksu(num) :
    cnt = 0
    for i in range(1, num + 1) :
        if num % i == 0 :
            cnt += 1
    return cnt

def solution(left, right):
    answer = 0

    for i in range(left, right + 1) :
        if yaksu(i) % 2 == 0 :
            answer += i
        else :
            answer -= i

    return answer

if __name__ == '__main__' :
    left_1 = 13
    right_1 = 17
    left_2 = 24
    right_2 = 27

    print(solution(left_1, right_1))