# TODO Напишите функцию для поиска индекса товара
def search_items(lists_, item):
    if item in lists_:
        return lists_.index(item)

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
#print(items_list)
#print()
items = ['банан', 'груша', 'персик']
for find_item in items:
    index_item = search_items(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

