"""
3. Усовершенствовать родительский класс таким образом, чтобы получить доступ к защищенным переменным.
Результат выполнения заданий 1 и 2 должен быть идентичным.
"""


class ItemDiscount:
    __name = "good_01"
    __price = 100

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'наименование товара: {super().get_name()}, цена: {super().get_price()}')


print("результат работы метода дочернего класса:")
ItemDiscountReport().get_parent_data()
print("результат получения значения переменных через родительский класс:")
print(f'{ItemDiscount().get_name()}, {ItemDiscount().get_price()}')



