# TODO Напишите функцию для поиска индекса товара
def index_tovara(spisok, towar):
    if towar in spisok:
        for index in range(0, len(spisok)):
            if spisok[index] == towar:
                return index
    else:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = index_tovara(items_list, find_item)   # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
