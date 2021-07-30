def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            answer = False
            break
    return answer

def solution_later(phone_book):
    phone_book = sorted(phone_book, key=len)
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True