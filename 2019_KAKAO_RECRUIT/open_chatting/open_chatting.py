def solution(record) :
    answer = []
    dic = {}

    for cmd in record :
        if cmd.split(' ')[0] == 'Enter' or cmd.split(' ')[0] == 'Change' :
            dic[cmd.split(' ')[1]] = cmd.split(' ')[2]

    for cmd in record :
        if cmd.split(' ')[0] == 'Enter' :
            answer.append("{}님이 들어왔습니다.".format(dic[cmd.split(' ')[1]]))
        elif cmd.split(' ')[0] == 'Leave' :
            answer.append("{}님이 나갔습니다.".format(dic[cmd.split(' ')[1]]))
        else :
            pass

    return answer

if __name__ == '__main__' :
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    print(solution(record))