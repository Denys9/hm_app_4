try:
    sum = 0
    num = int(input('Введіть число - '))
    while True:
            num = int(input('Введіть число - '))
            if num != 7:
                if num >0:
                    print('Number is positive')
                if num < 0:
                    print('Number is negative')
                if num == 0:
                    print('Number is equal to zero')
            else:
                print('Good bye!')
except Exception as ex:
    print(f'Eror information: {ex}')
finally:
    print('Exit')
