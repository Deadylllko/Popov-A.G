import math
t1k1=int(input("Введите длину катета"))
t1k2=int(input("Введите длину катета"))
t2k1=int(input("Введите длину катета"))
t2k2=int(input("Введите длину катета"))
gip1=math.sqrt(t1k1**2+t1k2**2)
gip2=math.sqrt(t2k1**2+t2k2**2)
print(f"Гипотенуза первого треугольника{gip1}")
print(f"Гипотенуза второго треугольника{gip2}")
if gip1>gip2:
    print("Гипотенуза первого треугольника больше")
    print("Гипотенуза второго треугольника меньше")
else:
    print("Гипотенуза второго треугольника больше")
    print("Гипотенуза первого треугольника меньше")


n=int(input("Введите количество символов"))
a=[]
for i in range(n):
    a.append(input("Введите символ"))
for i in range(n):
    for j in range(i+1,n):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
for i in range(n):
    print(a[i])