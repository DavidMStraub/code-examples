# Eingabe
# Hinweis: wir nehmen an, dass "temperaturen" mindestens einen Wert enthält
temperaturen = [15.2, 16.8, 14.5, 18.3, 17.1, 16.9, 15.8]

# Verarbeitung

anzahl_ueber_16 = 0
summe_temperaturen = 0
temp_min = temperaturen[0]
temp_max = temperaturen[0]

for temperatur in temperaturen:

    # Berechnung der Anzahl der Werte über 16 °C
    if temperatur > 16:
        anzahl_ueber_16 += 1

    # Berechnung der Summe aller Temperaturen
    summe_temperaturen += temperatur

    # Berechnung des Minimums
    if temperatur < temp_min:
        temp_min = temperatur

    # Berechnung des Maximums
    if temperatur > temp_max:
        temp_max = temperatur

# Berechnung der Durchschnittestemp.
anzahl_werte = len(temperaturen)
temp_durchschnitt = summe_temperaturen / anzahl_werte


# Ausgabe
print(f"Durchschnittstemperatur: {temp_durchschnitt:.2f} °C")
print(f"Maximaltemperatur: {temp_max:.2f} °C")
print(f"Minimaltemperatur: {temp_min:.2f} °C")
print(f"Anzahl der Werte über 16 °C: {anzahl_ueber_16}")
