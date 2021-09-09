"""3. Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря."""
from random import sample


def random_generator(num_start, num_end, size):

    if num_end == 0:
        print("Pls input number greater than zero")
        exit()

    rand_list_generated = sample(range(num_start, num_end), size)
    rand_dict_generated = {}
    number = 1

    for element in rand_list_generated:
        key = f'elem_{number}'
        rand_dict_generated[key] = element
        number += 1

    return rand_list_generated, rand_dict_generated


start_input = 1
end_input = 1000
size_input = 10

rand_list, rand_dict = random_generator(start_input, end_input, size_input)

print(rand_list)
print(rand_dict)
