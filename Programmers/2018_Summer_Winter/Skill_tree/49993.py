from collections import deque

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees :
        skill_line = deque(skill)

        for skill_name in skills :
            if skill_name in skill :
                if skill_name != skill_line.popleft() :
                    break
        else :
            answer += 1

    return answer

if __name__ == '__main__' :
    skill = "CBD"
    skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

    print(solution(skill, skill_trees))