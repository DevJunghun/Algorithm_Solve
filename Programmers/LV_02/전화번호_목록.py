def solution(phone_book):
    new_phone_book = sorted(phone_book)
    answer = True
    for i in range(len(new_phone_book) - 1):
        head = new_phone_book[i]
        if new_phone_book[i + 1][:len(head)] == head:
            answer = False
            break
    return answer