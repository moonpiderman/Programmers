def solution_other(cacheSize, cities):
    answer = 0
    cache = [' '] * cacheSize

    for city in cities :
        city = city.lower()
        if city in cache :
            answer += 1
            cache.remove(city)
            cache.append(city)
        else :
            answer += 5
            cache.append(city)
            cache.pop(0)
    return answer

def solution(cacheSize, cities) :
    answer = 0
    cache = []

    if cacheSize == 0 :
        return len(cities) * 5

    for city in cities :
        city = city.lower()
        if not city in cache :
            if len(cache) < cacheSize :
                answer += 5
                cache.append(city)
            else :
                answer += 5
                cache.pop(0)
                cache.append(city)
        else :
            answer += 1
            cache.remove(city)
            cache.append(city)

    return answer

if __name__ == '__main__' :
    cacheSize_1 = 3
    cities_1 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

    cacheSize_2 = 3
    cities_2 = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]

    cacheSize_3 = 2
    cities_3 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]

    cacheSize_4 = 5
    cities_4 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]

    cacheSize_5 = 2
    cities_5 = ["Jeju", "Pangyo", "NewYork", "newyork"]

    cacheSize_6 = 0
    cities_6 = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

    print(solution(cacheSize_1, cities_1))
    print(solution(cacheSize_2, cities_2))
    print(solution(cacheSize_3, cities_3))
    print(solution(cacheSize_4, cities_4))
    print(solution(cacheSize_5, cities_5))
    print(solution(cacheSize_6, cities_6))
