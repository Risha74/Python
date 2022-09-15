tiket = int(input("Введите количество приобретаемых билетов "))
age = list(map(int, input("Введите возраст каждого посетителя через пробел ").split()))
s = 0

for i in age:
    if i < 18:
        s += 0
    elif 18 <= i <=25:
        s += 990
    elif i > 25:
        s += 1390

if tiket > 3:
    s = 0.9 * s

print("Сумма к оплате: ", s)