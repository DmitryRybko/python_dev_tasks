"""
2. Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False.
"""


def division_check(number):
    input_num = number
    is_int = "дробное"

    numb_split = input_num.split(".")
    int_part = numb_split[0]
    try:
        fract_part = numb_split[1]
    except IndexError:
        fract_part = 0
        is_int = "целое"

    int_fract_coincide = int_part == fract_part

    print(f'введено {is_int} число: {number}')
    print(f'целая часть: {int_part}')
    print(f'дробная часть: {fract_part}')
    if is_int == "дробное":
        print(f'числа до и после запятой совпадают: {int_fract_coincide}')
    print()
    pass


# user_input = input("Введите число: ")

user_input = '2034'
division_check(user_input)

user_input = '1035.345'
division_check(user_input)

user_input = '678'
division_check(user_input)

user_input = '548.548'
division_check(user_input)

user_input = '0.0'
division_check(user_input)
