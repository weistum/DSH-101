list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
player_in_team = len(list_players) // 2  # Определение количества игроков в команде

print(list_players[:player_in_team])
print(list_players[player_in_team:])
