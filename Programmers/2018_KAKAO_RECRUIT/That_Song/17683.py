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

def solution_fail_too(m, musicinfo):
    answer = ('(None)', None)
    m = code_change(m)
    for info in musicinfo:
        sp, ep, title, codes = info.split(',')
        sp_h, sp_m, ep_h, ep_m = map(int, sp.split(':') + ep.split(':'))
        time = 60 * (ep_h - sp_h) + (ep_m - sp_m)
        codes = code_change(codes)
        melody = (codes * time)[:time]
        if m in melody:
            if (answer[1] == None) or (time > answer[1]):
                answer = (title, time)
    return answer[0]

def solution(m, musicinfo):
    scales = {
        "C#": "H",
        "D#": "I",
        "F#": "J",
        "G#": "K",
        "A#": "L",
    }
    for _from, _to in scales.items():
        m = m.replace(_from, _to)

    max_played, answer = 0, "(None)"
    for info in musicinfo:
        start, end, title, scale = info.split(',')
        for _from, _to in scales.items():
            scale = scale.replace(_from, _to)
        during_music = len(scale)

        s_h, s_m = start.split(':')
        e_h, e_m = end.split(':')
        play_time = (int(e_h) - int(s_h)) * 60 + int(e_m) - int(s_m)

        real_play_time = scale * (play_time // during_music)

        diff = play_time % during_music
        real_play_time += scale[:diff]

        if m in real_play_time and play_time > max_played:
            max_played = play_time
            answer = title
    return answer

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