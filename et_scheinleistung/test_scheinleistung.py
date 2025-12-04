"""Unit-Tests für das scheinleistung-Modul.

Dieses Modul enthält Unit-Tests für die Funktionen zur Berechnung elektrischer
Leistung, einschließlich Tests für Wirkleistung, Blindleistung und deren Summe,
die der Gesamtleistung entsprechen sollte.

Um diese Tests auszuführen, verwenden Sie pytest:
    pytest test_scheinleistung.py

Oder mit ausführlicher Ausgabe:
    pytest -v test_scheinleistung.py
"""

import numpy as np
import scheinleistung


def test_leistung_equals_sum():
    """Testet, dass die Momentanleistung gleich der Summe von Wirkleistung und Blindleistung ist."""
    t = np.linspace(0, 1, 100)
    phi = np.pi / 6

    # Berechne die Komponenten
    momentanleistung = scheinleistung.leistung(t, phi)
    wirkleistung = scheinleistung.wirkleistung(t, phi)
    blindleistung = scheinleistung.blindleistung(t, phi)

    # Teste ob die Summe der Gesamtleistung entspricht
    np.testing.assert_allclose(
        wirkleistung + blindleistung, momentanleistung, atol=1e-15
    )
