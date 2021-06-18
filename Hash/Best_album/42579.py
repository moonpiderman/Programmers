def solution(genres, plays):
    answer = []
    total_plays = {}
    numbering = {}

    for i in range(len(genres)) :
        genre = genres[i]
        play = plays[i]
        total_plays[genre] = total_plays.get(genre, 0) + play
        numbering[genre] = numbering.get(genre, []) + [(play, i)]

    genreSort = sorted(total_plays.items(), reverse=True)

    for (genre, counts) in genreSort :
        numbering[genre] = sorted(numbering[genre], key=lambda x: (-x[0], x[1]))
        answer += [ i for play, i in numbering[genre][:2] ]

    return answer

if __name__ == '__main__' :
    genres_1 = ["classic", "pop", "classic", "classic", "pop"]
    plays_1 = [500, 600, 150, 800, 2500]

    print(solution(genres_1, plays_1))