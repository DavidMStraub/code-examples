# constants
FOOT = 0.3048  # meters
NAUTICAL_MILE = 1852  # meters
HOUR = 3600  # seconds
KNOT = NAUTICAL_MILE / HOUR  # meters per second
KILOMETER = 1000  # meters
KM_H = KILOMETER / HOUR  # meters per second

# input/output
choice = input(
    """Wählen Sie, welche Einheit Sie umrechnen möchten:
1: Fuß in Meter
2: Seemeilen in Meter
3: Knoten in Kilometer pro Stunde
"""
)
if choice not in ("1", "2", "3"):
    print("Ungültige Auswahl. Bitte wählen Sie 1, 2 oder 3.")
    exit()

value = float(input("Geben Sie den Wert ein, den Sie umrechnen möchten: "))

if choice == "1":
    result = value * FOOT
    print(f"{value} Fuß sind {result:.2f} Meter.")
elif choice == "2":
    result = value * NAUTICAL_MILE
    print(f"{value} Seemeilen sind {result:.2f} Meter.")
elif choice == "3":
    result = value * KNOT / KM_H
    print(f"{value} Knoten sind {result:.2f} Kilometer pro Stunde.")
