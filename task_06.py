"""
Задание 6. На закрепление навыков работы с очередью
Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока
Реализуйте класс-структуру "доска задач".
Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку
После реализации структуры, проверьте ее работу на различных сценариях
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
# На доработку OFF, решенные ON

class Tasks:
    def __init__(self):
        self.basic = []
        self.mod = []
        self.finish = []
        self.n_basic = 0

    def bases_push(self, name, el):
        self.basic.append((name, el))
        self.n_basic += 1
        for i in self.basic:
            if i[1] == 'OFF':
                self.mod.append((i[0], i[1]))
                self.basic.pop()
            elif i[1] == 'ON':
                self.finish_push(i[0], i[1])
                self.basic.pop()

    def mod_push(self, name, el):
        for i in self.mod:
            if self.mod[-1][0] == name:
                self.mod.pop()
                self.finish.append((name, el))
            else:
                self.mod.insert(0, self.mod.pop())

    def finish_push(self, name, el):
        self.finish.append((name, el))

    def stack_size(self):
        return f'Задач базовых было: {self.n_basic} ' \
               f'\nЗадач на добаботку: {len(self.mod)} ' \
               f'\nЗадач решенных: {len(self.finish)}'

    def all_tasks(self):
        return f'На добаботку: {self.mod} ' \
               f'\nРешенные: {self.finish}'


TSK = Tasks()

TSK.bases_push('task_01', 'ON')
TSK.bases_push('task_02', 'OFF')
TSK.bases_push('task_03', 'ON')
TSK.bases_push('task_04', 'OFF')
TSK.bases_push('task_05', 'OFF')
TSK.bases_push('task_06', 'OFF')

# TSK.mod_push('task_02', 'ON')
TSK.mod_push('task_05', 'ON')
TSK.mod_push('task_04', 'ON')

print(TSK.stack_size())
print(TSK.all_tasks())
