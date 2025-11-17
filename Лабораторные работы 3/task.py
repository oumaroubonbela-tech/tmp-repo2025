# TODO Напишите функцию find_common_participants
def find_common_participants(list1, list2, comma = ','):
    list_1 = list1.split(comma)
    #print(list_1)
    list_2 = list2.split(comma)
    common_participants = (set(list_1).intersection(list_2))
    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров,Сидоров,Смирнов"

inter_participants = find_common_participants(participants_first_group, participants_second_group)
print(inter_participants)
# TODO Проверьте работу функции с разделителем отличным от запятой
