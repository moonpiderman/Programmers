def solution(seoul):
    for mr in range(len(seoul)) :
        if seoul[mr] == "Kim" :
            answer = "김서방은 " + str(mr) + "에 있다"

    return answer


if __name__ == '__main__' :
    seoul = ["Jane", "Kim"]

    print(solution(seoul))