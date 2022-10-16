salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
index = 1+increase
need_money = 0  # количество денег, чтобы прожить 10 месяцев
i = 0
# TODO Оформить решение
for _ in range(1, months + 1):
  need_money += spend
  need_money -= salary
  spend *=index


print(round(need_money))
