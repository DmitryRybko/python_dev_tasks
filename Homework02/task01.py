"""
1. Проверить механизм наследования в Python. Для этого создать два класса.
Первый — родительский (ItemDiscount), должен содержать статическую информацию о товаре: название и цену.
Второй — дочерний (ItemDiscountReport), должен содержать функцию (get_parent_data),
отвечающую за отображение информации о товаре в одной строке.
Проверить работу программы, создав экземпляр (объект) родительского класса.
"""


class ItemDiscount:
    name = "good_01"
    price = 100


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'наименование товара: {super().name}, цена: {super().price}')


print("результат работы метода дочернего класса:")
ItemDiscountReport().get_parent_data()
print("результат получения значения переменных через родительский класс:")
print(f'{ItemDiscount().name}, {ItemDiscount().price}')


