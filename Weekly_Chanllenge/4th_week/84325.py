def solution(table, languages, preference):
    answer = []
    dic = {}
    pre = {}
    maxi = 0

    for i in range(len(languages)):
        pre[languages[i]] = preference[i]

    for i in range(len(table)):
        li = table[i].split()
        table[i] = li
        dic[li[0]] = 0

    for i in range(len(table)):
        for j in range(1, 6):
           if table[i][j] in pre.keys():
               dic[table[i][0]] += pre[table[i][j]] * (6 - j)

    s_dict = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    answer.append(s_dict[0][0])
    for i in range(1, len(s_dict)):
        if s_dict[0][1] == s_dict[i][1]:
            answer.append(s_dict[i][0])

    answer.sort()

    return answer[0]

if __name__ == '__main__':
    table_1 = [
        "SI JAVA JAVASCRIPT SQL PYTHON C#",
        "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
        "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
        "GAME C++ C# JAVASCRIPT C JAVA"
    ]

    languages_1 = ["PYTHON", "C++", "SQL"]

    preference_1 = [7, 5, 5]

    table_2 = [
        "SI JAVA JAVASCRIPT SQL PYTHON C#",
        "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
        "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
        "GAME C++ C# JAVASCRIPT C JAVA"
    ]

    languages_2 = ["JAVA", "JAVASCRIPT"]

    preference_2 = [7, 5]

    # print(solution(table_1, languages_1, preference_1))
    print(solution(table_2, languages_2, preference_2))
