import re
def solution(files):
    answer = []
    # 정규식에 맞춰 숫자를 기준으로 나열
    tmp = [ re.split(r"([0-9]+)", s) for s in files ]
    # print(tmp)

    # 문제에 맞게 정렬
    sort = sorted(tmp, key = lambda x: (x[0].lower(), int(x[1])))
    # print(sort)

    # 문자열로 바꿔서 출력
    answer = ["".join(s) for s in sort]

    return answer

if __name__ == '__main__' :
    files_1 = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    files_2 = ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]

    print(solution(files_1))
    print(solution(files_2))