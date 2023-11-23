ievade=int(input("Ievadi skaitli"))
summa=1
for skaitlis in range(1,ievade+1):
    summa=skaitlis*summa
print("Faktoriāls skaitlim",ievade,"ir",summa)