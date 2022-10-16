def sum_num(sn, n, sn1=0, n1=0):
    if n > 0 and n1 >= 0:
        n -= 1
        if n1 % 2 == 1:
            sn1 -= sn / 2 ** n1
            n1 += 1
        elif n1 % 2 == 0:
            sn1 += sn / 2 ** n1
            n1 += 1
        return sum_num(sn, n, sn1, n1)
    print(sn1)


start = 1
steps = int(input('Введите количество элементов: '))

sum_num(start, steps)
