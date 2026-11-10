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
import random

def naloga6():
    stevilo = random.randint(1, 100)
    poskusi = 0

    while poskusi < 7:
        try:
            ugibanje = int(input(f"Poskus {poskusi + 1}: "))
        except ValueError:
            print("To ni število!")
            continue

        poskusi += 1

        if ugibanje < stevilo:
            print("Več!")
        elif ugibanje > stevilo:
            print("Manj!")
        else:
            print(f"Bravo! Uganil si v {poskusi} poskusih.")
            return

    print("Porabil si vseh 7 poskusov.")
    print("Pravilno število je bilo:", stevilo)


#naloga6()

def cena_s_popustom(cena, popust):
    return cena * (1 - popust / 100)


slusalke = cena_s_popustom(40, 25)
miska = cena_s_popustom(20, 10)
podloga = cena_s_popustom(8, 0)

skupaj = slusalke + miska + podloga

print(f"Skupaj: {skupaj:.2f} EUR")


            
def je_prastevilo(n):
    if n < 2:
        return False

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def prastevila_med(a, b):
    seznam = []

    for n in range(a, b + 1):
        if je_prastevilo(n):
            seznam.append(n)

    return seznam



prastevila = prastevila_med(1, 1000)
print("Praštevil do 1000:", len(prastevila))

koraki = [8200, 10500, 12000, 10900, 6400, 11000, 13200]
def dni_nad_ciljem(koraki, cilj):
    print(dni_nad_ciljem(koraki, 10000)) 
    print(round(povprecje(koraki), 2))     
    print(najvec(koraki))

naloga9()                


            
