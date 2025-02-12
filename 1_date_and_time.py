"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import datetime, timedelta, date


def print_days():
    dt_now = datetime.now()
    delta = timedelta(days=1)
    print(dt_now + delta)
    print(dt_now)
    delta = timedelta(days=30)
    print(dt_now - delta)


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
    return dt


if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
