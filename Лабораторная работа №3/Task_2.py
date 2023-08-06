# TODO Напишите функцию find_common_participants
def find_common_participants(groop_1, groop_2, del_=","):
    list_groop_1 = groop_1.split(del_)  # Перенос перечисленых участников в список
    list_groop_2 = groop_2.split(del_)
    common_participants = list()  # Создание пустого списка для хранения повторяющихся участников
    for person in range(len(list_groop_1)):
        check_person = list_groop_1[person]  # Переменная хранит фамилию проверяемого участника
        if check_person in list_groop_2:  # Проверка наличия участника в другом списке
            common_participants.append(check_person)
    return common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group, "|"))
