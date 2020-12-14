max = 0
chislo = int(input("введите любое число: "))
while (chislo != 0):
    a = chislo % 10
    if (a > max):
        max = a
    chislo = chislo // 10
print ("максимальное число: ",max)