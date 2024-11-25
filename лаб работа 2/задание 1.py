money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0
while True:
    budget = salary + money_capital
    if budget >= spend:
        months += 1
        money_capital += salary - spend
        spend *= (1 + increase)
    else:
        break


# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

print("Количество месяцев, которое можно протянуть без долгов:", months)
