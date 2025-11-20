"""Funktionen fürs Würfelspiel "Pig"."""

import random


def wuerfle():
    """Würfle eine Zahl zwischen 1 und 6."""
    return random.randint(1, 6)

def spiele_runde(anzahl_wuerfe):
    """Spiele eine Runde.
    
    Rückgabe: Tuple aus Punktzahl und Liste der gewürfelten Augen.
    """
    punkte = 0
    augen_liste = []
    for _ in range(anzahl_wuerfe):
        augenzahl = wuerfle()
        augen_liste.append(augenzahl)
        if augenzahl == 1:
            punkte = 0
            break
        punkte += augenzahl
    return punkte, augen_liste

def spiele_strategie(max_wuerfe, ziel_punkte):
    """Spiele ein komplettes Spiel.
    
    Eingabeparameter:
    - `max_wuerfe`: Maximale Anzahl der Würfe pro Runde
    - `ziel_punkte`: Anzahl der Punkte, die zum Sieg erreicht werden
      müssen.

    Rückgabe: Anzahl der Runden bis zum Erreichen der Siegpunktzahl
    """
    gesamt_punkte = 0
    runden = 0
    while gesamt_punkte < ziel_punkte:
        punkte, _ = spiele_runde(max_wuerfe)
        runden += 1
        gesamt_punkte += punkte
    return runden
