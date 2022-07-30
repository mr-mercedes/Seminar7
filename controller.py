import input_data
import output_data
import logger


def click():
    accept = 'да'
    while accept == 'да':
        result = input_data.user_choice()
        match result:
            case 1:
                phone_book = input_data.user_book()
                logger.logger_address(phone_book)
            case 2:
                output_data.output_find()
            case 3:
                output_data.output_all()
            case 4:
                logger.logger_del()
        accept = input('Вы хотите еще что-то сделать? Да/Нет: ').lower()
    print('Всего доброго.')



