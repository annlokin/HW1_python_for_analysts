# Дан список с затратами на рекламу. Но в данных есть ошибки, некоторые затраты имеют отрицательную величину. 
# Удалите такие значения из списка и посчитайте суммарные затраты
# [100, 125, -90, 345, 655, -1, 0, 200]

# array = [100, 125, -90, 345, 655, -1, 0, 200]
# list_comp = [a for a in array if a > 0]
# print(sum(list_comp))

list_costs=[100, 125, -90, 345, 655, -1, 0, 200]
costs=[i for i in list_costs if i>0]
print(f"Сумма затрат на рекламу равна {sum(costs)}")