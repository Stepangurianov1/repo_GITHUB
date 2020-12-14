vir = int(input("введите выручку: "))
izd = int(input("введите издержки: "))
if (vir > izd):
    print("предприятие отработало в плюс")
    rent = vir / izd
    print(f"рентабильность: {rent:.3f}")
    chislo = int(input("введите колличество сотрудников: "))
    prib = vir - izd
    men_prib = prib / chislo
    print(f"прибыль на человека: {men_prib:.3f}")
elif(vir == izd): 
    print("предприятие в нуле")
else:
    print("предприятие отработало в минус")
