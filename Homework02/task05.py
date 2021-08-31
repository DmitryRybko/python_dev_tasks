"""
5. Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний класс.
Выполнить перегрузку методов конструктора дочернего класса
(метод init, в который должна передаваться переменная — скидка),
и перегрузку метода str дочернего класса.
В этом методе должна пересчитываться цена и возвращаться результат — цена товара со скидкой.
Чтобы все работало корректно, не забудьте инициализировать дочерний и родительский классы
(вторая и третья строка после объявления дочернего класса).
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

    def __init__(self, discount):
        super(ItemDiscountReport, self).__init__()
        self.discount = discount

    def __str__(self):
        self.discounted_price = super().price*(100-self.discount)/100
        return f'цена со скидкой: {self.discounted_price}'

    def get_parent_data(self):
        print(f'наименование товара: {super().name}, цена: {super().price}')


print("результат работы метода дочернего класса:")
ItemDiscountReport(20).get_parent_data()
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
ItemDiscountReport(20).get_parent_data()
print("результат получения значения переменных через родительский класс:")
print(f'{ItemDiscount().name}, {ItemDiscount().price}')

print()
print(ItemDiscountReport(20))
