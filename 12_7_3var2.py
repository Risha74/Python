per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада:"))

depozit = [int(per_cent['ТКБ']*money/100), int(per_cent['СКБ']*money/100), int(per_cent['ВТБ']*money/100), 
           int(per_cent['СБЕР']*money/100)]

print(depozit)

print("Максимальная сумма, которую вы можете забрать - ", max(depozit))
