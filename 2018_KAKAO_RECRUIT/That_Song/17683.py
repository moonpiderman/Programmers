def solution_fail(m, musicinfos):
    answer = ''
    scales = {
        'C': '0',
        'C#': '1',
        'D': '2',
        'D#': '3',
        'E': '4',
        'F': '5',
        'F#': '6',
        'G': '7',
        'G#': '8',
        'A': '9',
        'A#': 'A',
        'B': 'B'
    }

    # m을 16진수법으로 변환
    m_change = ''
    for s in m:
        if s in scales.keys():
            m_change += scales[s]

    print(m_change)

    # musicinfo를 16진법으로 변환
    for info in musicinfos:
        tmp = info.split(',')
        time = int(tmp[1][3:]) - int(tmp[0][3:])
        change = ''
        for al in tmp[3]:
            if al in scales.keys():
                change += scales[al]
        print(change)

    return answer

def code_change(line):
    if 'C#' in line : line.replace('C#', 'c')
    if 'D#' in line : line.replace('D#', 'd')
    if 'F#' in line : line.replace('F#', 'f')
    if 'G#' in line : line.replace('G#', 'g')
    if 'A#' in line : line.replace('A#', 'a')
    return line

def solution(m, musicinfo):
    answer = ('(None)', None)
    m = code_change(m)
    for info in musicinfo:
        sp, ep, title, codes = info.split(',')
        sp_h, ep_h, sp_m, ep_m = map(int, sp.split(':') + ep.split(':'))
        time = 60 * (ep_h - sp_h) + (ep_m - sp_m)
        line = code_change(info)
        melody = (line * time)[:time]
        if m in melody:
            if (answer[1] == None) or (time > answer[1]):
                answer = (title, time)
    return answer[0]

if __name__ == '__main__' :
    m_1 = "ABCDEFG"
    musicinfos_1 = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

    m_2 = "CC#BCC#BCC#BCC#B"
    musicinfos_2 = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

    m_3 = "ABC"
    musicinfos_3 = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

    print(solution(m_1, musicinfos_1))
    print(solution(m_2, musicinfos_2))
    print(solution(m_3, musicinfos_3))