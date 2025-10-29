list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]
Total_player = len(list_players)
middle = int((Total_player)/2)
Team_1 = list_players[:middle]
Team_2 = list_players[middle:]
print(Team_1)
print(Team_2)