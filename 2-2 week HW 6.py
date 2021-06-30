
#1 var
def int_func():
    word = input("1. введите слова со строчной буквой на Latin через пробел: ")
    print (word.title())
    return
int_func()


#2 var
def int_func():
    for word in input("2. введите слова со строчной буквой на Latin через пробел: ").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <=122:
                chars += 1
        print(word.title() if chars == len(word) else f"{word} - только прописные буквы")

int_func()
