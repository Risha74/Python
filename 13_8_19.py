tiket = int(input("Введите количество приобретаемых билетов "))
age = list(map(int, input("Введите возраст каждого посетителя через пробел ").split()))
summ = 0

for i in age:
    if i < 18:
        summ += 0
    elif 18 <= i <=25:
        summ += 990
    elif i > 25:
        summ += 1390

if tiket > 3:
    summ = 0.9 * summ

print(f"Сумма к оплате: {summ} рублей")