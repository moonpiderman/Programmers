def solution(record):
    answer = []
    check = []
    dic = {}

    for i in range(len(record)):
        check = record[i].split(' ')
        cmd = check[0]
        uid = check[1]

        if cmd != 'Leave':
            nick = check[2]
            # cmd_nick = [cmd, nick]
        else:
            nick = dic[uid][-1]
            # cmd_nick = [cmd, nick]

        if uid in dic:
            # dic[uid].append(cmd)
            dic[uid].append(nick)
        else:
            dic[uid] = [nick]
        print(dic)
        # cmd에 따라 출력할 것 만들어주기

        check.clear()
    return answer

if __name__ == '__main__' :
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    # record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    solution(record)