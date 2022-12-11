def rec_sum(n, s=0):
    x, y = divmod(n, 10)
    s += y
    if x == 0:
        return print(s)
    else:
        rec_sum(x, s)


rec_sum(int(input()))

def f(x):
    n=int(input('Введите число: '))
    if n == 0:
        return x
    x.append(n)
    return f(x)

a=[]
a=f(a)
a.sort()
print('Второе максимальное число: ',a[-2])
