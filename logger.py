import input_data


def logger_address(some_address):
    with open('phone_book.txt', 'a', encoding='UTF-8') as file:
        file.writelines(f'{some_address}\n')


def logger_del():
    with open('phone_book.txt', 'r', encoding='UTF-8') as file:
        tmp_book = file.read()

    user_input = input('Введите имя контакта для удаления: ')
    index_start = tmp_book.find(user_input)
    index_finish = tmp_book.find('\n', index_start)
    print(tmp_book[index_start - 8:index_finish - 1])
    new_book = tmp_book[:index_start - 9] + tmp_book[index_finish:]
    accept = input('Подтвердите удаление. Да/Нет: ').lower()

    if accept == 'да':
        with open('phone_book.txt', 'w', encoding='UTF-8') as file2:
            file2.writelines(f'{new_book}\n')

    print('Запись успешно удалена.')
