def nums(n, n1, sum_n=0):
    if n > 0:
        sum_n += n
        n -= 1
        return nums(n, n1, sum_n)
    if sum_n == (n1 * (n1 + 1) / 2):
        print('Равенство выполняется')
    else:
        print('Равенство НЕ выполняется')


num = 995 # maximum recursion depth exceeded in comparison
nums(num, num)
