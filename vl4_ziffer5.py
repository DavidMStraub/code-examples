"""Skript: Hausaufgabe

Wieviele Zahlen existieren zwischen 100 und 1000, die genau eine 5 als
Ziffer enthalten.
"""

loesung = 0
for zahl in range(100, 1001):
    zahl_string = str(zahl)

    anzahl_fuenfer = 0
    for ziffer_string in zahl_string:
        if ziffer_string == "5":
            anzahl_fuenfer += 1

    if anzahl_fuenfer == 1:
        loesung += 1
        print(f"Gefunden: {zahl}")

print(f"Es gibt {loesung} Zahlen.")
