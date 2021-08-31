"""
3. Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить.
"""


def zip_lists_to_dict(list_keys, list_values):
    result_dict = dict(zip(list_keys, list_values))
    len_keys = len(list_keys)
    len_dict = len(result_dict)
    len_diff = len_keys - len_dict
    if len_diff > 0:
        for i in range(len_dict, len_keys):
            result_dict[list_keys[i]] = None
    print(result_dict)
    pass


print("количество ключей и значений равно")
list_keys_01 = ["key01", "key02", "key03"]
list_values_01 = ["value01", "value02", "value03"]
zip_lists_to_dict(list_keys_01, list_values_01)

print("ключей больше чем значений")
list_keys_01 = ["key01", "key02", "key03", "key04"]
list_values_01 = ["value01", "value02"]
zip_lists_to_dict(list_keys_01, list_values_01)

print("значений больше чем ключей")
list_keys_01 = ["key01", "key02"]
list_values_01 = ["value01", "value02", "value03", "value04"]
zip_lists_to_dict(list_keys_01, list_values_01)