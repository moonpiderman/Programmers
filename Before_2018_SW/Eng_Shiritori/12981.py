def solution(n, words):
    answer = []
    stack = []
    member = {}
    for i in range(n) :
        tmp = []
        tmp.append(i + 1)
        tmp.append(0)
        member[(i+1) % n] = tmp

    for i in range(len(words)) :
        member[i % 3][1] += 1
        if not words[i] in stack :
            stack.append(words[i])
    # 중복 로직 넣기

    answer = member[len(words) % n]

    return answer

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