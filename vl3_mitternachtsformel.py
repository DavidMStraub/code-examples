"""Skript, das eine Funktion definiert, die die Lösungen der quadratischen
Gleichung ax²+bx+c=0 ausgibt."""


def mitternachtsformel(a, b, c):
    """Funktion die die Lösungen der quadratischen Gleichung ax²+bx+c=0 ausgibt.

    Eingabewerte: Parameter a, b, c (Float)
    Ausgabe: anzahl_lsg, x1, x2, wobei:
    - anzahl_lsg: Anzahl der Lösungen (0, 1 oder 2)
    - x1, x2: Ort der Nullstelle oder `None`
    """
    determinante = b**2 - 4 * a * c
    if determinante < 0:
        return 0, None, None  # 0 Lösungen
    elif determinante == 0:
        x1 = -b / (2 * a)
        return 1, x1, None
    # ab hier: nur falls determinante > 0
    x1 = (-b + determinante**0.5) / (2 * a)
    x2 = (-b - determinante**0.5) / (2 * a)
    return 2, x1, x2  # 2 Lösungen


ergebnis = mitternachtsformel(a=1, b=1, c=1)
print(f"a=1, b=1, c=1: Ergebnis ist {ergebnis}")
if ergebnis != (0, None, None):
    print("Fehler! Unerwartetes Ergebnis")


ergebnis = mitternachtsformel(a=1, b=2, c=1)
print(f"a=1, b=2, c=1: Ergebnis ist {ergebnis}")
if ergebnis != (1, -1, None):
    print("Fehler! Unerwartetes Ergebnis")


ergebnis = mitternachtsformel(a=1, b=2, c=1)
print(f"a=1, b=2, c=1: Ergebnis ist {ergebnis}")
if ergebnis != (1, -1, None):
    print("Fehler! Unerwartetes Ergebnis")


ergebnis = mitternachtsformel(a=1, b=3, c=1)
print(f"a=1, b=3, c=1: Ergebnis ist {ergebnis}")
anzahl_lsg, x1, x2 = ergebnis
print(f"x1: {x1:.5f}, erwartet: {-1.5 + 5**0.5 / 2:.5f}")
print(f"x2: {x2:.5f}, erwartet: {-1.5 - 5**0.5 / 2:.5f}")
