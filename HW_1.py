
a=int(input('Введите номер месяца: \n'))

if a in [1, 2, 12]:
    print('Winter')

elif a in [3, 4, 5]:
        print('Spring')

elif a in [6, 7, 8]:
        print('Summer')

elif a in [9, 10, 11]:
        print('Autumn')

else:
    print('Введите правильный номер')