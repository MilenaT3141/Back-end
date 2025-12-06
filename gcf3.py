liczba = int(input("Podaj cyfrę od 0 do 9: "))
proba = 1

while liczba != 7:
    liczba = int(input("Podaj cyfrę od 0 do 9: "))
    proba+=1

print("Brawo!")
print(f"Udało Ci się zgadanć w próbie nr {proba}")
