def symbols(s, st, s1):
    if s <= st:
        print(ord(chr(s)), '-', chr(s), end=' ')
        if (s1 - s - 1) % 10 == 0:
            print('\b')
        s += 1
        return symbols(s, st, s1)


start = 32
stop = 127
symbols(start, stop, start)
