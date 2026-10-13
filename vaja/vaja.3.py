import requests
"""
url = "https://api.frankfurter.dev/v1/latest"
odgovor = requests.get(url, params={"symbols": "USD,GBP,CHF,JPY"})

if odgovor.status_code != 200:
    print("napaka pri klicu API-ja.")
    exit()

podatki = odgovor.json()
tecaji = podatki["rates"]
print("Tečaji na dan", podatki["date"])

for valuta, tecaj in tecaji.items():
    print(valuta + ":", tecaj)

print("Skupaj valut :", len(tecaji))
"""
import requests

podatki = requests.get("https://api.frankfurter.dev/v1/latest").json()
tecaji = podatki["rates"]


def v_tujo(evri, valuta, tecaji):
    if valuta not in tecaji:
        return None
    return evri * tecaji[valuta]      # 1 EUR = tečaj, zato množimo


def v_evre(znesek, valuta, tecaji):
    if valuta not in tecaji:
        return None
    return znesek / tecaji[valuta]    # obratna smer, zato delimo
"""
evri = float(input("Znesek v EUR: "))
valuta = input("Valuta: ").upper()

tuje = v_tujo(evri, valuta, tecaji)

if tuje is None:
    print("Valuta", valuta, "ne obstaja.")
else:
    print(evri, "EUR =", round(tuje, 2), valuta)
    nazaj = v_evre(tuje, valuta, tecaji)
    print(round(tuje, 2), valuta, "=", round(nazaj, 2), "EUR")

"""
"""
url = "https://api.frankfurter.dev/v1/2026-09-01..2026-09-07"
podatki = requests.get(url, params={"symbols": "USD"}).json()
dnevi = podatki["rates"]          # datum -> {"USD": tečaj}

datumi = list(dnevi.keys())       # seznam, da lahko uporabljamo indekse

print(datumi[0] + ":", dnevi[datumi[0]]["USD"])

for i in range(1, len(datumi)):
    danes = dnevi[datumi[i]]["USD"]
    vceraj = dnevi[datumi[i - 1]]["USD"]

    if danes > vceraj:
        smer = "gor"
    else:
        smer = "dol"

    print(datumi[i] + ":", danes, "(" + smer + ")")

print("Podatki od", datumi[0], "do", datumi[-1] + ", skupaj", len(datumi), "dni")
"""
import requests

valute = ["USD", "GBP", "CHF"]

url = "https://api.frankfurter.dev/v1/latest"
podatki = requests.get(url, params={"symbols": ",".join(valute)}).json()
tecaji = podatki["rates"]

for a in valute:              # iz katere valute
    for b in valute:          # v katero valuto
        if a == b:
            continue          # USD -> USD nas ne zanima

        tecaj = tecaji[b] / tecaji[a]   # oba sta glede na EUR, zato ju delimo
        print("1", a, "=", round(tecaj, 4), b)
