"""Конвертер из формата CSV в JSON"""
# TODO импортировать необходимые молули
import csv
import json

#  Константы модуля
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


# TODO считать содержимое csv файла
# TODO Сериализовать в файл с отступами равными 4
def convert_file(csv_file, json_file):
    """
    Функция считывает файл в формате .csv
    и записывает в файл формата .json
    :param csv_file: Принимает файл из которого будет происходить чтение данных
    :param json_file: Файл в который будет производиться запись обработанных данных
    :return:
    """

    with open(csv_file) as csv_:
        lines = [line for line in csv.DictReader(csv_)]
        for line in lines[:4]:
            ...
    with open(json_file, 'w') as json_:
        json.dump(lines, json_, indent=4)


if __name__ == '__main__':  # Проверка работы программы

    convert_file(INPUT_FILENAME, OUTPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
