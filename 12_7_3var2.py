per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада:"))

depozit = [int(p[0]*money/100), int(p[1]*money/100), int(p[2]*money/100), int(p[3]*money/100)]

print(depozit)

print("Максимальная сумма, которую вы можете забрать - ", max(depozit))
