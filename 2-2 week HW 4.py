
#x = float(input('введите число: '))
#y = int(input('введите степень отрицальное число: '))

def my_func(a, b):
    try:
        a, b = float(a), int(b)
        if a <= 0 or b >= 0:
             return 'не выполнено условие, повторите ввод a>0, b<0'
        else:
            result = 1
            for i in range(abs(b)):
                result /= a
            return f'{a} ** {b} == : {round(result, 6)}'
            #result *= x
        #if y < 0:
            #result = 1 / result
    except ValueError:
        return "программа работает только с числом"

number_1 = input('введите число (a):  ')
number_2 = input('введите степень отрицальное число (b):  ')

#print(f'{x} ** {y} == ', power(x, y))

print(my_func(number_1, number_2))


