"""Skript um die Quersumme einer Zahl zu bestimmen."""

zahl = 7432

zahl_string = str(zahl)

quersumme = 0
for ziffer_string in zahl_string:
    ziffer = int(ziffer_string)
    quersumme = quersumme + ziffer

print(f"Die Quersumme von {zahl} beträgt {quersumme}.")