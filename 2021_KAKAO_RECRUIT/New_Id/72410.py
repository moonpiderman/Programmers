def solution(new_id):
    answer = ''
    new_id = new_id.lower()

    for word in new_id :
        if word.isalnum() or word in '-_.' :
            answer += word

    while '..' in answer :
        answer = answer.replace('..', '.')

    if answer[0] == '.' and len(answer) > 1 :
        answer = answer[1:]
    else :
        answer

    if answer[-1] == '.' :
        answer = answer[:-1]
    else :
        answer
    # answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    # answer = answer[:-1] if answer[-1] == '.' else answer

    # answer = 'a' if answer == '' else answer

    if len(answer) == 0 :
        answer = 'a'
    else :
        answer

    if len(answer) >= 16 :
        answer = answer[:15]
        if answer[-1] == '.' :
            answer = answer[:-1]

    if len(answer) <= 3 :
        answer = answer + answer[-1] * (3 - len(answer))

    return answer

if __name__ == '__main__' :
    new_id_1 = "...!@BaT#*..y.abcdefghijklm"
    new_id_2 = "z-+.^."
    new_id_3 = "=.="
    new_id_4 = "123_.def"
    new_id_5 = "abcdefghijklmn.p"

    print(solution(new_id_1))
    print(solution(new_id_2))
    print(solution(new_id_3))
    print(solution(new_id_4))
    print(solution(new_id_5))
