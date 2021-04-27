def solution(array, commands):
    return_length = len(commands)

    return_list = [0 for i in range(return_length)]

    for i in range(len(return_list)):
        # 임시 리스트 생성
        check_list = [0 for j in range(commands[i][1] - commands[i][0] + 1)]

        for k in range(len(check_list)):
            check_list[k] = array[commands[i][0] - 1 + k]
        check_list.sort()
        return_list[i] = check_list[commands[i][2] - 1]

    return return_list
