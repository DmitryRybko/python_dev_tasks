"""
4. Реализовать возможность переустановки значения цены товара. Необходимо, чтобы и родительский,
и дочерний классы получили новое значение цены.
Следует проверить это, вызвав соответствующий метод родительского класса и функцию дочернего
(функция, отвечающая за отображение информации о товаре в одной строке).
"""


class ItemDiscount:
    __name = "good_01"
    __price = 100

    @property
    def name(cls):
        return cls.__name

    @name.setter
    def name(cls, new_name):
        cls.__name = new_name

    @property
    def price(cls):
        return cls.__price

    @price.setter
    def price(cls, new_price):
        cls.__price = new_price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'наименование товара: {super().name}, цена: {super().price}')


print("результат работы метода дочернего класса:")
ItemDiscountReport().get_parent_data()
print("результат получения значения переменных через родительский класс:")
print(f'{ItemDiscount().name}, {ItemDiscount().price}')

print()
new_name = "good_02"
new_price = 200
print(f"меняем имя на {new_name}")
ItemDiscount.name = new_name
print(f"меняем цену на {new_price}")
ItemDiscount.price = new_price

print()
print("результат работы метода дочернего класса:")
ItemDiscountReport().get_parent_data()
print("результат получения значения переменных через родительский класс:")
print(f'{ItemDiscount().name}, {ItemDiscount().price}')
