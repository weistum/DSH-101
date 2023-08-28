""" Сумма произведений"""
import json


def sum_of_multiplicatin(json_file) -> float:
    """
  Функция вычисления суммы произведений из списка словарей
  :param json_file: Принимает файл с исходными данными для вычисления в формате .json.
   data -> list Принимает данные из файла в виде списка словарей.
   muilt_score -> list Формирует список из первых множителей.
   muilt_weight -> list Формирует список из вторых множителей.
   product_of_numbers -> int Хранит результат умножения, вычесленного для каждого словаря.
  :return: Возвращает сумму произведений чисел окуругленную до третьего знака.
  """

    with open(json_file) as file:
        data = json.load(file)
        muilt_score = [
            item[pos]
            for item in data
            for pos in item
            if pos == 'score'
        ]
        muilt_weight = [
            item[pos]
            for item in data
            for pos in item
            if pos == 'weight'
        ]
    result = 0
    for _ in range(len(muilt_score)):
        product_of_numbers = muilt_score[_] * muilt_weight[_]
        result += product_of_numbers
    return round(result, 3)


print(sum_of_multiplicatin("input.json"))
