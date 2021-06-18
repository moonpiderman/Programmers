def solution(genres, plays):
    answer = []
    total_plays = {}
    numbering = {}

    for i in range(len(genres)) :
        genre = genres[i]
        play = plays[i]
        total_plays[genre] = total_plays.get(genre, 0) + play
        numbering[genre] = numbering.get(genre, []) + [(play, i)]

    genreSort = sorted(total_plays.items(), key = lambda x: x[1], reverse=True)
    # 총 플레이 횟수를 기준으로 정렬한다.

    for (genre, counts) in genreSort :
        numbering[genre] = sorted(numbering[genre], key = lambda x: (-x[0], x[1]))
        # lambda에 -를 붙여줘야 내림차순으로 정렬가능하다.
        # 중간중간 print를 넣어서 확인 가능
        answer += [ i for play, i in numbering[genre][:2] ]

    return answer

if __name__ == '__main__' :
    genres_1 = ["classic", "pop", "classic", "classic", "pop"]
    plays_1 = [500, 600, 150, 800, 2500]

    print(solution(genres_1, plays_1))