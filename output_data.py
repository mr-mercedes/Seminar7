def output_all():
    with open('phone_book.txt', 'r', encoding='UTF-8') as file:
        all_book = file.read()
        print(all_book)


def output_find():
    with open('phone_book.txt', 'r', encoding='UTF-8') as file:
        find_name = file.readlines()
        user_input = input('Введите имя для поиска: ')
        for line in find_name:
            index_start = line.find(user_input)
            index_finish = line.find('\n', index_start)
            print(line[index_start - 8:index_finish - 1])
            break



