def solution_fail(n, words):
    stack = []
    member = {}
    for i in range(n) :
        tmp = []
        tmp.append(i + 1)
        tmp.append(0)
        member[(i + 1) % n] = tmp

    for i in range(len(words) - 1) :
        member[i % n][1] += 1
        if not words[i] in stack :
            stack.append(words[i])
    # print(member)
    if len(words) % n == 0 :
        if words[-1] in stack :
            answer = member[len(words) % n]
        else :
            answer = [0, 0]
    else :
        answer = member[len(words) % n]

    return answer

def solution(n, words):
    stack = []
    member, count = 0, 0

    stack.append(words[0])
    last_spell = words[0][-1]

    for i in range(1, len(words)) :
        if words[i] in stack or words[i][0] != last_spell :
            member = (i % n) + 1
            count = (i // n) + 1
            break
        else :
            stack.append(words[i])
            last_spell = words[i][-1]

    return [member, count]

if __name__ == '__main__' :
    n_1 = 3
    words_1 = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

    n_2 = 5
    words_2 = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]

    n_3 = 2
    words_3 = ["hello", "one", "even", "never", "now", "world", "draw"]

    print(solution(n_1, words_1))
    print(solution(n_2, words_2))
    print(solution(n_3, words_3))