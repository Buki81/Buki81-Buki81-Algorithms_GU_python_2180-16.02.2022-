class RES:

    def __init__(self):
        self.sign = 0
        self.n = 0
        self.m = 0

    def mark(self):
        self.sign = input('Введите операцию (+, -, *, /) или 0 для выхода: ')
        if self.sign == '0':
            return None
        elif self.sign in ('+*-/'):
            return RES.num1(self)
        else:
            return self.mark()

    def num1(self):
        self.n = input('Введите первое число: ')
        try:
            int(self.n)
            return RES.num2(self)
        except ValueError:
            print(f'{self.n} не число. Повторите ввод числа')
            return self.num1()

    def num2(self):
            self.m = input('Введите второе число: ')
            try:
                self.m = int(self.m)
            except ValueError:
                print(f'{self.m} не число. Повторите ввод числа')
                return self.num2()
            if self.sign == '/' and self.m == 0:
                print('На ноль делить нельзя! Повторите ввод числа')
                return self.num2()
            return self.res()

    def res(self):
        if self.sign == '+':
            print(int(self.n) + int(self.m))
            return self.mark()
        elif self.sign == '-':
            print(int(self.n) - int(self.m))
            return self.mark()
        elif self.sign == '*':
            print(int(self.n) * int(self.m))
            return self.mark()
        elif self.sign == '/':
            print(int(self.n) / int(self.m))
            return self.mark()


rs = RES()
rs.mark()
