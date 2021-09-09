"""
5. Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений
заменить на значения типа example345 (строка+число). Далее — усовершенствовать вторую функцию из предыдущего примера
(функцию извлечения данных). Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных подстрок на новое значение и вывод
всех подстрок, состоящих из букв и цифр и имеющих пробелы только в начале и конце — например, example345.
"""

import random
import re


def create_txt_file():
    try:
        with open("task5_txt_file.txt", 'x', encoding='UTF-8') as file:
            list_text = []
            list_nums = []

            text = "randomtext"
            list_nums = [random.randint(0, 100) for _ in range(10)]
            list_text = [random.choice(text)+str(list_nums[i]) for i in range(10)]

            print(f'создан текстовый список: {list_text}')
            print(f'создан числовой список: {list_nums}')

            result_lines = list(zip(list_text, list_nums))
            print(f'записываем в файл: {result_lines}')

            for line in result_lines:
                file.write(line[0] + " " + str(line[1]) + "\n")

    except FileExistsError:
        print("файл уже существует")

    print_txt_file("task5_txt_file.txt")


def print_txt_file(text_file):
    with open(text_file, 'r', encoding='UTF-8') as file:
        print()
        print("Содержимое файла:")
        lines = file.readlines()
        text_for_search = ""
        for line in lines:
            text_for_search += line
            print(line.strip())

        print()
        print("текст для поиска")
        print(text_for_search)
        substring_for_search = "x"

        print(f'поиск первого вхождения подстроки "{substring_for_search}":')
        search_first_instance = re.search(substring_for_search, text_for_search)
        print(search_first_instance)

        print()
        print(f'поиск всех вхождений подстроки "{substring_for_search}":')
        search_all_instances = re.findall(substring_for_search, text_for_search)
        print(search_all_instances)

        print()
        print(f'заменяем все найденные подстроки на новое значение:')
        resulting_text = re.sub('x', '_NEW_', text_for_search)
        print("измененный текст:")
        print(resulting_text)

        print(f'выводим все подстроки, состоящих из букв и цифр и имеющих пробелы только в начале и конце:')
        pattern = '\s([a-zA-Z]+\d\w*)\s'
        search_specific_substrings = re.findall(pattern, text_for_search)
        print(search_specific_substrings)


create_txt_file()
