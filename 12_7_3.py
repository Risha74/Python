per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада:"))

p = list(per_cent.values())

depozit = [int(money*i/100) for i in p]

print(depozit)

print("Максимальная сумма, которую вы можете забрать - ", max(depozit))
