"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте собственный класс-структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""
class StackLimit:
    def __init__(self):
        self.elems = []
        self.el0 = self.elems.append([])
        self.el1 = self.elems.append([])
        self.el2 = self.elems.append([])

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        if len(self.elems[0]) < 2:
            self.elems[0].append(el)
        elif len(self.elems[1]) < 2:
            self.elems[1].append(el)
        elif len(self.elems[2]) < 2:
            self.elems[2].append(el)

    def pop_out(self):
        if len(self.elems[2]) <= 2:
            return self.elems[2].pop()
        elif len(self.elems[1]) <= 2:
            return self.elems[1].pop()
        elif len(self.elems[0]) <= 2:
            return self.elems[0].pop()

    def get_val(self):
        if len(self.elems[2]) <= 2:
            return self.elems[2]
        elif len(self.elems[1]) <= 2:
            return self.elems[1]
        elif len(self.elems[0]) <= 2:
            return self.elems[0]

    def get_val1(self):
        return self.elems[0], self.elems[1], self.elems[2]

    def stack_size(self):
        return len(self.elems[0] + self.elems[1] + self.elems[1])


SL_OBJ = StackLimit()

# SL_OBJ.push_in(10)
# SL_OBJ.push_in(11)
# SL_OBJ.push_in(12)
# SL_OBJ.push_in(13)
# SL_OBJ.push_in(14)
# SL_OBJ.push_in(15)
# SL_OBJ.push_in(16)

SL_OBJ.push_in('10')
SL_OBJ.push_in('11')
SL_OBJ.push_in('12')
SL_OBJ.push_in('13')
SL_OBJ.push_in('14')
SL_OBJ.push_in('15')
SL_OBJ.push_in('16')

print(SL_OBJ.stack_size())
print(SL_OBJ.pop_out())
print(SL_OBJ.get_val())
print(*SL_OBJ.get_val1())
print(SL_OBJ.is_empty())
