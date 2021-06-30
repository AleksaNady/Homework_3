
def sum_number():
    i = 0
    while True:
        list_number = input("введите число или  Q для выхода из программы:   ").split()
        for num in list_number:
            if num.title() == "Q":
                return i
            else:
                try:
                    i += int(num)
                except ValueError:
                    print("для выхода нажмите на Q")
        print('итого сумма', {i})

print(sum_number())

