# import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_account:str)->str:
    """Функция принемает название карты или счета и маскирует номер"""
    result = ''
    words = card_account.split()
    if 'Счет' in words:
        number_mask = get_mask_account(words[-1])
    else:
        number_mask = get_mask_card_number(words[-1])
    for _ in words:
        if _.isalpha():
            result += _ + ' '

    return result + number_mask


def get_date(date:str)->str:
    """Функция принимает время и дату в формате Г.М.Д.: выводит в формате Д.М.Г."""
    day = date[8:10]
    month = date[5:7]
    year = date[:4]
    return f"{day}.{month}.{year}"
# def get_date(date):
    # date_obj = datetime.datetime.fromisoformat(date)
    # # date_obj = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    # # day = date_obj.day
    # # month = date_obj.month
    # # year = date_obj.year
    # date_str = date_obj.strftime('%d.%m.%Y')
    # return date_str



if __name__ == '__main__':
   print(mask_account_card("Счет 73654108430135874305"))
   print(get_date("2024-03-11T02:26:18.671407"))