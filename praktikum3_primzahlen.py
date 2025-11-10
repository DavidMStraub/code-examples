
def ist_prim(zahl):
    """Gibt aus, ob `zahl` eine Primzahl ist."""
    if zahl == 1:
        return False
    for teiler in range(2, zahl):
        if zahl % teiler == 0:
            return False
        if teiler**2 > zahl:
            break
    return True

def test_ist_prim():
    """Testfunktion für ist_prim ohne assert-Statement"""
    # Primzahlen
    for zahl in  [2, 3, 5, 7]:
        if not ist_prim(zahl):
            print(f"Fehler! {zahl} nicht als Primzahl erkannt!")
            return
    # keine Primzahlen
    for zahl in  [1, 4, 6, 8, 9]:
        if ist_prim(zahl):
            print(f"Fehler! {zahl} fälschlicherweise als Primzahl erkannt!")
            return
    print("Alle Zahlen von 1-9 korrekt erkannt.")

def test_ist_prim_assert():
    """Testfunktion für ist_prim mit assert-Statement"""
    # Primzahlen
    for zahl in  [2, 3, 5, 7]:
        assert ist_prim(zahl), f"{zahl} nicht als Primzahl erkannt!"
    # keine Primzahlen
    for zahl in  [1, 4, 6, 8, 9]:
        assert not ist_prim(zahl), f"{zahl} fälschlicherweise als Primzahl erkannt!"


if __name__ == "__main__":
    test_ist_prim_assert()
