from itertools import combinations
def solution(relation):
    row = len(relation)
    col = len(relation[0])
    key_idx = list(range(col))
    candidtate_keys = []

    if row == 1 : return col

    for i in range(1, col + 1) :
        for comb in combinations(key_idx, i) :
            hist = []
            for re in relation :
                current_key = [re[c] for c in comb]
                if current_key in hist :
                    break
                else :
                    hist.append(current_key)
            else :
                for ck in candidtate_keys :
                    if set(ck).issubset(set(comb)) :
                        break
                else :
                    candidtate_keys.append(comb)

    return len(candidtate_keys)


if __name__ == '__main__' :
    relation = [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"]
    ]

    print(solution(relation))