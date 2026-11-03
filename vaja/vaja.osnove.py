"""
doma = 3
gostje = 1


doma, gostje = gostje, doma

print("Popravljen rezultat:", doma, ":", gostje)

skupaj = doma + gostje
print("Skupaj:", skupaj)
"""
"""
minute = 4000

min = minute % 60
zure = minute // 60
ur = zure % 24
dan = zure// 24

print(dnevi, "dni,", ure, "ur,", minute_ostanek, "minut")
"""
"""
dijaki = 25
cena = 9.50


pice = round(dijaki/3 +0.5)
print(pice)
skupaj = pice * cena
print(skupaj)
na_dijaka = round(skupaj / dijaki,2)
print(na_dijaka)
"""
"""
starost = int(input("Starost: "))
dan = input("Dan: ").lower()

if starost < 0:
    print("Neveljavna starost.")

elif starost <= 5:
    cena = 0

elif starost <= 17:
    cena = 5

elif starost <= 64:
    cena = 8

else:
    cena = 6

if starost >= 0:
    if dan == "torek" and cena > 0:
        cena = cena - 2

    print("Cena:", cena, "EUR")
"""
"""
vsota = 0
e = 0
for i in range(1,61):
    if i % 7 == 0:
        continue
    else:
        e += 1
        vsota += i
        print(f"{i}. {vsota}")
        if vsota >= 1000:
            break
"""
import random as r

a = r.randint(1,100)

            
