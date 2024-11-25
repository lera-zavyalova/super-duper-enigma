salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
required_money_capital = 0
for month in range(months):
    if month > 0:
        spend *= (1 + increase)
    if spend > salary:
        required_money_capital += (spend - salary)

required_money_capital = round(required_money_capital)

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_money_capital)
