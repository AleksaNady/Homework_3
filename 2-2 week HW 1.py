#x = int(input("Введите больше 0 значение x = "))
#y = int(input("Введите больше 0 значение y = "))

def my_func(a, b):
    try:
        a = int(a)
        b = int(b)
        z = a / b
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return "делить на  0 запрещено,  повторите ввод b"
    return round(z,2)

print(my_func(input("Введите больше 0 значение a = "),input("Введите больше 0 значение b = ")))










