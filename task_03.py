"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
archiv = {'Кот': 32_500, 'Кит': 139_00, 'Жмот': 144_245, 'Скряга': 75_000, 'Врун': 97_840}
n = 3  # Выбрать 3 фирмы


def one(box, n):  # Суммарная O(n^2)
    archiv_val = list(box.values())  # O(n)
    archiv_key = list(box.keys())  # O(n)
    archiv_val.sort(reverse=True)  # O(n)
    archiv_top3 = []  # O(n)

    for i in range(n):  # O(n^2)
        archiv_top3.append(archiv_key[list(box.values()).index(archiv_val[i])])
    return archiv_top3


print(*one(archiv, n))


# --------------------------
def two(box, n):  # Суммарная O(n^3)
    lst = []
    for k, v in box.items():  # O(n)
        lst.append(v)
    lst.sort(reverse=True)  # O(n)
    archiv_top3 = []  # O(n)
    for i in range(n):  # O(n^3)
        for k, v in archiv.items():  # O(n)
            if v == lst[i]:  # O(n)
                archiv_top3.append(k)
    return archiv_top3


print(*two(archiv, n))
