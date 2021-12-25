def solution(s):
    arr = s.split(' ')
    result = []

    for word in arr:
        add_word = ""
        for i in range(len(word)):
            if i % 2 == 0:
                add_word += word[i].upper()
            else:
                add_word += word[i].lower()
        result.append(add_word)

    result = " ".join(result)
    return result
