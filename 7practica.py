import random as rd
l=[rd.randint(-10,10)for i in range(10)]
for i in range(len(l)-1):
    if l[i] < 0 and l[i + 1] < 0:
        print(l[i],l[i+1])
    else:
        None

l=map(int,input("Введите числа разделяя их пробелом").split())
m=[]
for x in l:
    if x not in m:
        m.append(x)
print(m)