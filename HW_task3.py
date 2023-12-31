# Даны два списка.
# Дата покупки
# ['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', '2021-09-30', '2021-12-22', '2021-11-29', '2021-12-24', '2021-11-26', '2021-10-27', '2021-12-18', '2021-11-09', '2021-11-23', '2021-09-27', '2021-10-02', '2021-12-27', '2021-09-20', '2021-12-13', '2021-11-01', '2021-11-09', '2021-12-06', '2021-12-08', '2021-10-09', '2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13', '2021-10-26', '2021-12-09']
# Суммы покупок по датам
# [1270, 8413, 9028, 3703, 5739, 4095, 295, 4944, 5723, 3701, 4471, 651, 7037, 4274, 6275, 4988, 6930, 2971, 6592, 2004, 2822, 519, 3406, 2732, 5015, 2008, 316, 6333, 5700, 2887]
# 4.1 Найдите, какая выручка у компании в ноябре
# Используйте list comprehensions
# 4.2 Найдите выручку компании в зависимости от месяца
# Для этого напишите функцию, которая на вход принимает список с датами и список с выручкой, а на выходе словарь, где ключи - это месяцы, а значения - это выручка.
# Используйте аннотирование типов.

list_date = ['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', '2021-09-30', '2021-12-22', '2021-11-29', '2021-12-24', '2021-11-26', '2021-10-27', '2021-12-18', '2021-11-09', '2021-11-23', '2021-09-27', '2021-10-02', '2021-12-27', '2021-09-20', '2021-12-13', '2021-11-01', '2021-11-09', '2021-12-06', '2021-12-08', '2021-10-09', '2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13', '2021-10-26', '2021-12-09']
list_sum = [1270, 8413, 9028, 3703, 5739, 4095, 295, 4944, 5723, 3701, 4471, 651, 7037, 4274, 6275, 4988, 6930, 2971, 6592, 2004, 2822, 519, 3406, 2732, 5015, 2008, 316, 6333, 5700, 2887]

revenue_november = sum([list_sum[i] for i in range(len(list_sum)) if '-11-' in list_date[i]])
print (f'Выручка в ноябре: {revenue_november}')

def revenue_monthly (list_date: list, list_sum: list) -> dict:
    result = {}

    for i in range(len(list_date)):
        month = list_date[i][5:7]

        if month in result:
            result[month] += list_sum[i]
        else: 
            result[month] = list_sum[i]
    return result

print (revenue_monthly(list_date,list_sum))