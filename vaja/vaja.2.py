1
"""
avto = {
    "znamka": "Mazda",
    "model": "RX7",
    "letnik": "2002",
    "barva": "bela"
}
print(avto["znamka"])
print(avto["model"])
print(avto["letnik"])
print(avto["barva"])
for kljuc, vrednost in avto.items():
    print(kljuc, "->", vrednost)
"""
"""
sola = {
    "ime": "ŠC Kranj",
    "naslov": {
        "ulica": "Kidričeva cesta 55",
        "posta": 4000,
        "kraj": "Kranj"
    },
    "smeri": ["računalništvo", "elektrotehnika", "mehatronika"]
}

print(sola["naslov"]["posta"])  
print(sola["smeri"][-1])         
print(len(sola["smeri"]))

for vrednost in sola["smeri"]:
    print(vrednost)
"""
2
"""
import requests

url = "https://api.open-meteo.com/v1/forecast"

parametri = {
    "latitude": 46.292608,
    "longitude": 14.429896,
    "current": "temperature_2m,wind_speed_10m"
}
odgovor = requests.get(url, params=parametri)
print(odgovor.status_code)
podatki = odgovor.json()
print(podatki)

temperatura = podatki["current"]["temperature_2m"]
enota = podatki["current_units"]["temperature_2m"]
print(f"V Tupaličah je trenutno {temperatura} {enota}.")

veter = podatki["current"]["wind_speed_10m"]
enotav = podatki["current_units"]["wind_speed_10m"]
print(f"V Tupaličah je trenutno {veter} {enotav}.")
"""
3
"""
import requests

def trenutna_temperatura(lat, lon):
    url = "https://api.open-meteo.com/v1/forecast"
    parametri = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m"
    }
    odgovor = requests.get(url, params=parametri)
    podatki = odgovor.json()
    return podatki["current"]["temperature_2m"]


kraji = {
    "Ljubljana": (46.0569, 14.5058),
    "Maribor": (46.5547, 15.6459),
    "Tupalice": (46.292608, 14.429896)
}
temperature = {}
for ime, (lat, lon) in kraji.items():
    t = trenutna_temperatura(lat, lon)
    temperature[ime] = t

print(temperature)
"""
"""
temperature = {
    "Ljubljana": 14.2,
    "Maribor": 15.1,
    "Koper": 18.4,
    "Kamnik": 12.9,
    "Tupalice": 16.7,
    "Kranj": 18
}

najtoplejse = "Ljubljana"
najvisja = temperature["Ljubljana"]

for mesto, t in temperature.items():
    if t < najvisja:
        najvisja = t
        najtoplejse = mesto

print(f"Najtoplejše: {najtoplejse} ({najvisja} °C)")
"""
import requests

mesta = {
    "Ljubljana":  (46.0569, 14.5058),
    "Maribor":    (46.5547, 15.6459),
    "Kranj":      (46.2389, 14.3556),
    "Celje":      (46.2361, 15.2675),
    "Koper":      (45.5481, 13.7302),
    "Velenje":    (46.3592, 15.1103),
    "Novo mesto": (45.8040, 15.1689),
    "Ptuj":       (46.4200, 15.8700),
    "Trbovlje":   (46.1550, 15.0533),
    "Kamnik":     (46.2259, 14.6121),
}

temperature = {}

for mesto, (lat, lon) in mesta.items():
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current=temperature_2m"
    )

    podatki = requests.get(url).json()
    temperatura = podatki["current"]["temperature_2m"]

    temperature[mesto] = temperatura

# Najtoplejše in najhladnejše mesto
najtoplejse = max(temperature, key=temperature.get)
najhladnejse = min(temperature, key=temperature.get)

# Povprečna temperatura
povprecje = sum(temperature.values()) / len(temperature)

# Izpis temperatur
for mesto, temperatura in temperature.items():
    print(f"{mesto}: {temperatura} °C")

print()
print(f"Najtoplejše mesto: {najtoplejse} ({temperature[najtoplejse]} °C)")
print(f"Najhladnejše mesto: {najhladnejse} ({temperature[najhladnejse]} °C)")
print(f"Povprečna temperatura: {povprecje:.1f} °C")
