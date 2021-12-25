def solution(s, n):
    answer = ""

    for alpha in s :
        if alpha == " " :
            answer += alpha
            continue

        if alpha.islower() :
            if (ord(alpha) + n) > ord('z') :
                alpha = chr((ord(alpha) + n) - ord('z') + ord('a') - 1)
            else :
                alpha = chr(ord(alpha) + n)
        elif alpha.isupper() :
            if (ord(alpha) + n) > ord('Z') :
                alpha = chr((ord(alpha) + n) - ord('Z') + ord('A') - 1)
            else :
                alpha = chr(ord(alpha) + n)

        answer += alpha

    return answer


if __name__ == '__main__' :
    s_1 = "AB"
    n_1 = 1
    s_2 = "z"
    n_2 = 1
    s_3 = "a B z"
    n_3 = 4

    print(solution(s_3, n_3))