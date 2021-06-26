def solution(s):
    answer = ''
    s = s.lower()
    string = s.split(' ')

    for word in string :
        word = list(word)
        if word[0].isdigit() :
            word.append(" ")
            answer += "".join(word)
            continue
        else :
            word[0] = word[0].upper()
            word.append(" ")
            answer += "".join(word)

    answer = list(answer)
    del answer[-1]
    answer = "".join(answer)

    return answer

if __name__ == '__main__' :
    s_1 = "3people unFollowed me"
    s_2 = "for the last week"

    print(solution(s_2))