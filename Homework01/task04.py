"""
4. Написать программу «Банковский депозит». Она должна состоять из функции и ее вызова с аргументами.
Клиент банка делает депозит на определенный срок.
В зависимости от суммы и срока вклада определяется процентная ставка:
1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 % годовых).
10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 года – 6.5 % годовых).
100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 года — 7.5 % годовых).
Необходимо написать функцию, в которую будут передаваться параметры: сумма вклада и срок вклада.
Каждый из трех банковских продуктов должен быть представлен в виде словаря с ключами (begin_sum, end_sum, 6, 12, 24).
Ключам соответствуют значения начала и конца диапазона суммы вклада и значения процентной ставки для каждого срока.
В функции необходимо проверять принадлежность суммы вклада к одному из диапазонов и
выполнять расчет по нужной процентной ставке. Функция возвращает сумму вклада на конец срока.
"""


def bank_deposit(amount, term):
    """
    рассчитывается сумма вклада на конец срока без капитализации
    """
    bank_deposit_small = {"begin_sum": 1000, "end_sum": 10000, "6": 0.05, "12": 0.06, "24": 0.05}
    bank_deposit_medium = {"begin_sum": 10000, "end_sum": 100000, "6": 0.06, "12": 0.07, "24": 0.065}
    bank_deposit_large = {"begin_sum": 100000, "end_sum": 1000000, "6": 0.07, "12": 0.08, "24": 0.075}
    interest_amount = 0

    if bank_deposit_small["begin_sum"] <= amount < bank_deposit_small["end_sum"]:
        rate = bank_deposit_small[term]
        interest_amount = amount * rate * int(term)/12

    elif bank_deposit_medium["begin_sum"] <= amount < bank_deposit_medium["end_sum"]:
        rate = bank_deposit_medium[term]
        interest_amount = amount * rate * int(term)/12

    elif bank_deposit_large["begin_sum"] <= amount < bank_deposit_large["end_sum"]:
        rate = bank_deposit_medium[term]
        interest_amount = amount * rate * int(term)/12

    else:
        return f"сумма депозита {amount} вне допустимого диапазона"

    return amount + int(interest_amount)


amount_input_1 = 2000
amount_input_2 = 20000
amount_input_3 = 200000
amount_input_4 = 200

term_1 = "24"
term_2 = "12"
term_3 = "6"
term_4 = "6"

return_amount_1 = bank_deposit(amount_input_1, term_1)
return_amount_2 = bank_deposit(amount_input_2, term_2)
return_amount_3 = bank_deposit(amount_input_3, term_3)
return_amount_4 = bank_deposit(amount_input_4, term_4)

print(return_amount_1)
print(return_amount_2)
print(return_amount_3)
print(return_amount_4)
