def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True

if __name__ == '__main__':
    books = [
        ["119", "97674223", "1195524421"],
        ["123", "456", "789"],
        ["12", "123", "1235", "567", "88"]
    ]

    for book in books:
        print(solution(book))