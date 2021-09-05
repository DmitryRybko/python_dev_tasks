"""
6. Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два класса.
Инициализировать классы необязательно.
Внутри каждого поместить функцию get_info, которая в первом классе будет отвечать за вывод названия товара,
а вторая — его цены. Далее реализовать выполнение каждой из функции тремя способами.
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


class ItemNameReport(ItemDiscount):

    def get_info(self):
        print(f'наименование товара: {super().name}')


class ItemPriceReport(ItemDiscount):

    def get_info(self):
        print(f'цена: {super().price}')


class ItemDataReport(ItemNameReport, ItemPriceReport):

    def get_info(self):
        super().get_info()


def get_data(input_class):
    input_class.get_info()


print("вариант 1")
print(ItemNameReport().get_info())
print(ItemPriceReport().get_info())

print()
print("вариант 2")
get_data(ItemNameReport())
get_data(ItemPriceReport())

print()
print("вариант 3")
for item in (ItemNameReport(), ItemPriceReport()):
    print(item.get_info())