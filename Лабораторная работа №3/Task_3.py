# TODO  Напишите функцию count_letters
def count_letters(txt):
    dict_letters = {}  # Создание нового словаря для хранения количества букв.
    low_txt = txt.lower()  # Перевод всего текста в нижний регистр.
    for i, letter in enumerate(low_txt):
        if letter.isalpha():  # Проверка является ли символ буквой.
            if letter in dict_letters:
                dict_letters[letter] += 1  # Если буква есть в словаре, увеличить значение счетчика.
            else:
                dict_letters[letter] = 1  # Если буквы в словаре нет, создать новый элемент словаря.
    return dict_letters


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_):
    dict_mode = count_letters(dict_)
    total_quality_letters = sum(dict_mode.values())  # Расчет общего количества букв.
    for key in dict_mode:
        dict_mode[key] /= total_quality_letters  # Преобразуем количество букв в в коэффициент частотности
    return dict_mode


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
result = calculate_frequency(main_str)
for item in result.items():
    print(f"{item[0]}: {item[1]:.2f}")
