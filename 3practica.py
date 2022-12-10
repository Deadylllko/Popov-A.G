n = int(input("Введите количество долек"))
m = int(input("Введите количество долек"))
k = int(input("Введите количество долек"))
if k < n * m and ((k % n==0 ) or (k % m==0)):
    print("Да")
else:
    print("Нет")