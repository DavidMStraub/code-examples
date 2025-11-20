"""Tests fürs Würfelspiel "Pig"."""

import random

import pig_funktionen


def test_wuerfle():
    random.seed(17)
    augen = []

    # Würfle 1000 mal
    for _ in range(1000):
        augen.append(pig_funktionen.wuerfle())

    # Checke, dass die Augenzahl immer >= 1 ist
    assert min(augen) == 1

    # Checke, dass die Augenzahl immer <= 6 ist
    assert max(augen) == 6

    # Checke, dass die Resultate ungefähr gleichverteilt sind
    assert 3.3 < sum(augen) / 1000 < 3.7


def test_spiele_runde():
    random.seed(17)
    for anzahl_wuerfe in range(10):
        punktzahl, augen_liste = pig_funktionen.spiele_runde(anzahl_wuerfe)

        # stelle sicher, dass punktzahl eine nicht-negative int ist
        assert isinstance(punktzahl, int)
        assert punktzahl >= 0

        # Stelle sicher, dass augen_liste die Liste der Würfe ist
        assert len(augen_liste) <= anzahl_wuerfe

        # Falls 1 gewürfelt wurde, checke Punktzahl = 0
        if 1 in augen_liste:
            assert punktzahl == 0


def test_spiele_strategie():
    random.seed(17)
    # Teste Werte auf Plausbilität
    runden_1wurf = pig_funktionen.spiele_strategie(max_wuerfe=1, ziel_punkte=100)
    assert runden_1wurf > 20
    assert runden_1wurf < 150
    runden_3wuerfe = pig_funktionen.spiele_strategie(max_wuerfe=3, ziel_punkte=100)
    assert runden_3wuerfe > 6
    assert runden_3wuerfe < 50
    assert runden_1wurf > runden_3wuerfe


if __name__ == "__main__":
    test_wuerfle()
    test_spiele_runde()
    test_spiele_strategie()

    # wenn ein assert "auslöst", kommen wir nicht bei diesem print an
    print("Alle Tests erfolgreich.")
