try:
    num = int(input('Введіть число - '))
    if num >>0 and num !=7:
        print('Number is positive')
    elif num << 0 and num !=7:
        print('Number is negative')
    elif num == 0:
        print('Number is equal to zero')
    elif num ==7:
        print('Good bye!')
except Exception as ex:
    print(f'Eror information: {ex}')
finally:
    print('Exit')