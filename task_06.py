from random import randint as rd


def guess_num(n, t, att=1):
    print(n)
    if att == 10:
        print(f'Вы НЕ угадали! Загаданное число {n}')
    elif n > t:
        att += 1
        print(f'Загаданное число больше Вашего. \nВаша попытка №{att}')
        t = int(input('Угадайте целое число от 0 до 100 за 10 попыток: '))
        return guess_num(n, t, att)
    elif n < t:
        att += 1
        print(f'Загаданное число меньше Вашего. \nВаша попытка №{att}')
        t = int(input('Угадайте целое число от 0 до 100 за 10 попыток: '))
        return guess_num(n, t, att)
    elif n == t:
        print(f'Вы угадали! Загаданное число {n}')


txt = int(input('Угадайте целое число от 0 до 100 за 10 попыток: '))
num = rd(0, 100)
guess_num(num, txt)
