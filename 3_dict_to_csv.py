"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv

job_list = [
    {'name': 'John', 'age': 35, 'job': 'driver'},
    {'name': 'Jane', 'age': 30, 'job': 'doctor'},
    {'name': 'Mark', 'age': 25, 'job': 'manager'},
    {'name': 'Terry', 'age': 37, 'job': 'actor'},
]


def main(dict_list):
    with open('job_list.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for job in dict_list:
            writer.writerow(job)


if __name__ == "__main__":
    main(job_list)
