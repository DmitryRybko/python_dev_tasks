"""
2. Инкапсулировать оба параметра (название и цену) товара родительского класса.
Убедиться, что при сохранении текущей логики работы программы будет сгенерирована ошибка выполнения.
"""


class ItemDiscount:
    __name = "good_01"
    __price = 100


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(f'наименование товара: {super().__name}, цена: {super().__price}')


print("результат работы метода дочернего класса:")
ItemDiscountReport().get_parent_data()
print("результат получения значения переменных через родительский класс:")
print(f'{ItemDiscount().__name}, {ItemDiscount().__price}')


