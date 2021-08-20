"""
5. Усовершенствовать программу «Банковский депозит».
Третьим аргументом в функцию должна передаваться фиксированная ежемесячная сумма пополнения вклада.
Необходимо в главной функции реализовать вложенную функцию подсчета процентов для пополняемой суммы.
Примем, что клиент вносит средства в последний день каждого месяца, кроме первого и последнего.
Например, при сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев.
Вложенная функция возвращает сумму дополнительно внесенных средств (с процентами),
а главная функция — общую сумму по вкладу на конец периода.
"""


def bank_deposit(amount, term, add_amount):

    """
    рассчитывается сумма вклада на конец срока без капитализации, с ежемесячным начислением процентов и
    возможностью пополнения в течение срока вклада.
    """

    bank_deposit_small = {"begin_sum": 1000, "end_sum": 10000, "6": 0.05, "12": 0.06, "24": 0.05}
    bank_deposit_medium = {"begin_sum": 10000, "end_sum": 100000, "6": 0.06, "12": 0.07, "24": 0.065}
    bank_deposit_large = {"begin_sum": 100000, "end_sum": 1000000, "6": 0.07, "12": 0.08, "24": 0.075}
    interest_amount = 0

    def additional_amount_calc(additional_amount, term, rate):
        add_interest = 0
        for n in range(int(term)-2):
            add_interest += additional_amount*(n+1)*rate/12

        total_add_accrual = additional_amount*(int(term)-2) + add_interest
        return total_add_accrual

    if bank_deposit_small["begin_sum"] <= amount < bank_deposit_small["end_sum"]:
        rate = bank_deposit_small[term]
        interest_amount = amount * rate * int(term)/12
        total_addition_accrual = additional_amount_calc(add_amount, term, rate)

    elif bank_deposit_medium["begin_sum"] <= amount < bank_deposit_medium["end_sum"]:
        rate = bank_deposit_medium[term]
        interest_amount = amount * rate * int(term)/12
        total_addition_accrual = additional_amount_calc(add_amount, term, rate)

    elif bank_deposit_large["begin_sum"] <= amount < bank_deposit_large["end_sum"]:
        rate = bank_deposit_medium[term]
        interest_amount = amount * rate * int(term)/12
        total_addition_accrual = additional_amount_calc(add_amount, term, rate)

    else:
        return f"сумма депозита {amount} вне допустимого диапазона"



    return amount + int(interest_amount) + int(total_addition_accrual)


amount_input_1 = 2000
amount_input_2 = 20000
amount_input_3 = 200000
amount_input_4 = 200

amount_add = 500

term_1 = "24"
term_2 = "12"
term_3 = "6"
term_4 = "6"

return_amount_1 = bank_deposit(amount_input_1, term_1, amount_add)
return_amount_2 = bank_deposit(amount_input_2, term_2, amount_add)
return_amount_3 = bank_deposit(amount_input_3, term_3, amount_add)
return_amount_4 = bank_deposit(amount_input_4, term_4, amount_add)

print(return_amount_1)
print(return_amount_2)
print(return_amount_3)
print(return_amount_4)
