def enter(cmd, uid, nickname) :
    value = []
    return value

def leave(cmd, uid) :
    value = []
    return value

def change(cmd, uid, nickname) :
    value = []
    return value

def solution(record):
    answer = []
    check = [] # split을 진행하기 위한 체크

    #
    # uid 부분을 key 값으로해서 딕셔너리를 만들고
    # cmd 부분과 nickname 부분을 split으로 나눠서 풀어보는 것이 좋을듯하다.

    for i in range(len(record)) :
        check = record[i].split(' ')
        print(check)
        check.clear()

    return answer

if __name__ == '__main__' :
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    solution(record)