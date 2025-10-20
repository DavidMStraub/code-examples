"""Skript, das die Lösungen der quadratischen Gleichung ax²+bx+c=0 bestimmt."""

def mitternachtsformel(a, b, c):
    """Funktion, die die sungen der quadratischen Gleichung ax²+bx+c=0 bestimmt.

    Argumente:
    - a, b, c: Koeffizienten der quadratischen Gleichung ax²+bx+c=0

    Ausgabe: anzahl_lsg, x1, x2, wobei:
    - anzahl_lsg: Anzahl der Lösungen
    - x1: erste Nullstelle oder None, falls es keine Lösung gibt
    - x2: zweite Nullstelle oder None, falls es eine oder keine Lösung gibt
    """
    diskriminante = b**2 - 4 * a * c
    if diskriminante < 0:
        return 0, None, None
    elif diskriminante == 0:
        x1 = -b / (2 * a)
        return 1, x1, None
    # Standardfall D > 0
    x1 = (-b + diskriminante**0.5) / (2 * a)
    x2 = (-b - diskriminante**0.5) / (2 * a)
    return 2, x1, x2


def test_mitternachtsformel(a, b, c):
    ergebnis = mitternachtsformel(a, b, c)
    print(f"Ergebnis für a={a}, b={b}, c={c}: {ergebnis}")


test_mitternachtsformel(1, 1, 1)
test_mitternachtsformel(1, 2, 1)
test_mitternachtsformel(2, 5, 2)
