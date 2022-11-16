def chek_input(string_, element):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#""$%^&*()-_+={[}]\|/?.>,<:;'
    is_error = False
    for i in string_:
        if i in letters:
            print('Введенная последовательность не отвечает заданным условиям')
            is_error = True
            break
    for j in element:
        if j in letters:
            print('Введенное число не отвечает заданным условиям')
            is_error = True
            break
    return is_error

def BubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if array[middle] == element:
        if middle >= 1:
            return middle-1, middle+1
        elif middle < 1:
            return f'Число {element} меньше минимального в списке'
        elif middle == len(array):
            return f'Число {element} больше максимального в списке'
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


num = input('Введите числа через пробел')
el = input('Введите число')

if chek_input(num, el):
    raise SystemExit

element = int(el)
numb = list(map(int, num.split()))

print(BubbleSort(numb))

numb.append(element)
BubbleSort(numb)
print(binary_search(numb, element, 0, len(numb)))
