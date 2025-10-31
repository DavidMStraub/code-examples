"""Skript, das das Laden einer Batterie simuliert."""

spannung_start = 3.0  # V
spannung_stop = 4.2  # V
spannung_limit = 4.5  # V
max_schritte = 50

spannung = spannung_start
schritt = 0

while spannung < spannung_stop and schritt < max_schritte:
    schritt += 1
    spannung += 0.1
    if schritt % 5 == 0:
        print(f"Ladungsschritt {schritt}: Spannung = {spannung:.1f} V")
    if spannung >= spannung_limit:
        print("Warnung: Spannung überschreitet das Limit!")
        break

print(f"Endspannung nach {schritt} Schritten: {spannung:.1f} V")
