"""
4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
Если файл с таким именем уже существует, выводим соответствующее сообщение.
Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
Для создания списков использовать генераторы. Применить к спискам функцию zip().
Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
чтобы каждая строка файла содержала текстовое и числовое значение.
Вызвать вторую функцию. В нее должна передаваться ссылка на созданный файл.
Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
Вся программа должна запускаться по вызову первой функции.
"""

import random


def create_txt_file():
    try:
        with open("task4_txt_file.txt", 'x', encoding='UTF-8') as file:
            list_text = []
            list_nums = []

            text = "randomtext"
            list_text = [random.choice(text) for i in range(10)]
            list_nums = [random.randint(0, 100) for _ in range(10)]

            print(f'создан текстовый список: {list_text}')
            print(f'создан числовой список: {list_nums}')

            result_lines = list(zip(list_text, list_nums))
            print(f'записываем в файл: {result_lines}')

            for line in result_lines:
                file.write(line[0] + " " + str(line[1]) + "\n")

    except FileExistsError:
        print("файл уже существует")

    print_txt_file("task4_txt_file.txt")
    pass


def print_txt_file(text_file):
    with open(text_file, 'r', encoding='UTF-8') as file:
        print()
        print("Содержимое файла:")
        lines = file.readlines()
        for line in lines:
            print(line.strip())
    pass


create_txt_file()
