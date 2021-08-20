"""
1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
Первый и второй множитель должны задаваться в виде аргументов функции.
Значения каждой строки таблицы должны быть представлены списком, который формируется в цикле.
После этого осуществляется вызов внешней lambda-функции, которая формирует на основе списка строку.
Полученная строка выводится в главной функции.
Элементы строки (элементы таблицы умножения) должны разделяться табуляцией.
"""

x_input = 5
y_input = 5


def multiplication_table(a, b):
    x = a
    y = b

    for item_x in range(1, x + 1):
        result_list = []
        for item_y in range(1, y + 1):
            result_list.append(item_x * item_y)
        result_str = line_str(result_list)
        print(result_str)


line_str = lambda result_line: '\t'.join(str(element) for element in result_line)
multiplication_table(x_input, y_input)
