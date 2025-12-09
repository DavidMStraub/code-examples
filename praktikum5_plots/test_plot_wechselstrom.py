"""Einfache Tests für die Funktionen im Modul plot_wechselstrom"""

import plot_wechselstrom

def test_spannung():
    # Spannung bei t=0
    u = plot_wechselstrom.spannung(0)
    # Muss 0 sein
    assert u == 0
    # Strom bei t=0
    i = plot_wechselstrom.strom(0, 0)
    assert i == 0
    # Für phi>0 ist i nicht mehr 0
    i = plot_wechselstrom.strom(0, phi=0.1)
    assert i > 0

if __name__ == "__main__":
    test_spannung()
