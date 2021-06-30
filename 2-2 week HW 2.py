name = (input('Имя: '))
age = int(input('Возврат: '))
city = (input('Город: '))
email = (input('E-mail: '))
phone = int(input('Moб.тел: '))

def person_info (name, age, city, email, phone):
    print(f'{name}, {age} год(а) проживает в городе {city}, контактные данные: e-mail {email},телефон {phone}')

person_info (name, age, city, email, phone)
