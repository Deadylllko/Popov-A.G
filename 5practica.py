N=int(input("Введите число не меньшее 2"))
i=1
while i<=N:
    i=i+1
    if N%i==0:
        print("Наименьший натуральный делитель:", i )
        break
