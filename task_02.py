def num(n, ev, od):
    if n > 0:
        digit = n // 10
        remnant = n % 10
        if remnant % 2 == 0:
            ev += 1
        elif remnant % 2 == 1:
            od += 1
        return num(digit, ev, od)
    print(f'Четных цифр - {ev}\nНечетных цифр  - {od}')


number = int(input('Введите число: '))
even, odd = 0, 0
num(number, even, odd)
