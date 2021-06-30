a = int(input('введите а: '))
b = int(input('введите b: '))
c = int(input('введите c: '))

def two_of_three(a, b, c):
    num1 = max(a, b)
    num2 = max(b, c)
    print('1 max значение', num1)
    print('1 max значение', num2)
    return num1 + num2

print('итого результат', two_of_three(a, b, c))