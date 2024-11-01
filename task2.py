# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, razdelitel=','):
    words1, words2 = first_group.split(razdelitel), second_group.split(razdelitel)
    spisok = set(words1).intersection(words2)
    spisok_ = list(spisok)
    spisok_.sort()

    return spisok_

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group, participants_second_group,'|'))