money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
i = money_capital
index = 1 + increase
month = 0  # количество месяцев, которое можно прожить

while i >= spend:
    i += 5000
    i-=spend
    spend *= index
    month += 1



print(month)
