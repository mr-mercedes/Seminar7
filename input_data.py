def user_book():
    telephone_book = \
        {
            'Имя': input('Введите имя: '),
            'Фамилия': input('Введите фамилию: '),
            'Телефон': input('Введите телефон: '),
            'Комментарий': input('Введите комментарий: '),
        }
    print('Запись успешно добавлена.')

    return telephone_book


def user_choice():
    choices = \
        {
            1: 'Добавить запись',
            2: 'Поиск контакта по имени',
            3: 'Вывести весь справочник',
            4: 'Удалить запись'
        }
    print('Что вы хотите сделать ?\n')

    for v, k in choices.items():
        print(f'{v}:{k}')

    operation = int(input('Введите цифру операции: '))

    return operation



