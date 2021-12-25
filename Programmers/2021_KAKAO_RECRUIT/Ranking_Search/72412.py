from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

def make_cases(tmp):
    cases = []
    for k in range(5):
        for li in combinations([0, 1, 2, 3], k):
            case = ''
            for idx in range(4):
                if idx not in li:
                    case += tmp[idx]
                else:
                    case += '-'
            cases.append(case)
    return cases

def solution(info, query):
    answer = []
    all_ppl = {}
    for i in info:
        seperate_info = i.split()
        cases = make_cases(seperate_info)
        for case in cases:
            if case not in all_ppl.keys():
                all_ppl[case] = [int(seperate_info[4])]
            else:
                all_ppl[case].append(int(seperate_info[4]))

    for key in all_ppl.keys():
        all_ppl[key].sort()

    for q in query:
        seperate_q = q.split()
        target = seperate_q[0] + seperate_q[2] + seperate_q[4] + seperate_q[6]
        if target in all_ppl.keys():
            answer.append(len(all_ppl[target]) - bisect_left(all_ppl[target], int(seperate_q[7]), lo=0, hi=len(all_ppl[target])))
        else:
            answer.append(0)
    return answer

def solution_diff(info, query):
    answer = []
    info_dict = defaultdict(list)
    for i in info:
        i = i.split()
        i_key = i[:-1]
        i_val = int(i[-1])
        for idx in range(5):
            for c in combinations(i_key, idx):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(i_val)

    print(info_dict)

    for key in info_dict.keys():
        info_dict[key].sort()

    print(info_dict)

    for q in query:
        q = q.split(' ')
        q_score = int(q[-1])
        q = q[:-1]

        for i in range(3):
            q.remove('and')
        while '-' in q:
            q.remove('-')
        tmp_q = ''.join(q)

        if tmp_q in info_dict:
            score = info_dict[tmp_q]
            if len(score) > 0:
                start, end = 0, len(score)
                # lower bound
                while end > start:
                    mid = (start + end) // 2
                    if score[mid] >= q_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(score) - start)
        else:
            answer.append(0)
    return answer

def solution_fail(info, query):
    answer = []
    for q in query:
        condi = q.split()
        cnt = 0
        for chk in info:
            chkout = chk.split()
            if condi[0] != '-':
                if condi[0] != chkout[0]:
                    continue
            if condi[2] != '-':
                if condi[2] != chkout[1]:
                    continue
            if condi[4] != '-':
                if condi[4] != chkout[2]:
                    continue
            if condi[6] != '-':
                if condi[6] != chkout[3]:
                    continue
            if int(condi[7]) <= int(chkout[4]):
                cnt += 1
        answer.append(cnt)
    return answer

if __name__ == '__main__':
    info = [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"
    ]
    query = [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150"
    ]

    print(solution(info, query))