# организовать программу подсчета символов во введенном тексте
my_string = input('Введите свой произвольный текст: ')
res = len(my_string.split())
print('Количество символов в тексте: ', len(my_string))

# работа с методами строк
print('Верхний регистр:', my_string.upper())
print('Нижний регистр:', my_string.lower())
print('Строка без пробелов:', my_string.replace(' ',''))
print('Первый символ текста:', my_string[0])
print('Последний символ текста:', my_string[-1])