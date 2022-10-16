def num(n, st):
    if n > 0:
        a = n % 10
        b = n // 10
        st += str(a)
        return num(b, st)
    print(st)
    print(int(st))


m = int(input('Введите число, которое требуется перевернуть: '))
s = ''
num(m, s)
