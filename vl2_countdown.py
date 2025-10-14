"""Skript, das entscheiden soll, ob eine Rakete starten darf."""

# Eingaben
treibstoff_prozent = 100
temperatur_degc = 90
ist_crew_bereit = True
wetter = "storm"


if ist_crew_bereit:
    string_crew_bereit = "Crew ist bereit"
else:
    string_crew_bereit = "Crew ist nicht bereit"

print(
    f"Treibstoff ist bei {treibstoff_prozent:.2f}%, "
    f"Temperatur bei {temperatur_degc:.2f} °C, "
    f"{string_crew_bereit}, "
    f"Wetter ist {wetter}"
)

ist_start_freigegeben = True
if treibstoff_prozent < 99:
    print("Treibstofffüllmenge zu niedrig!")
    ist_start_freigegeben = False
elif not ist_crew_bereit:  # else if not is crew ready
    print("Crew ist nicht bereit!")
    ist_start_freigegeben = False
elif temperatur_degc >= 100:
    print("Temperatur zu hoch!")
    ist_start_freigegeben = False
elif wetter == "storm":
    print("Schlechtes Wetter!")
    ist_start_freigegeben = False

if ist_start_freigegeben:
    print("🚀 Start ist freigegeben!")
else:
    print("❌ Start abgebrochen!")