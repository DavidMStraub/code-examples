"""Funktionen fürs Würfelspiel "Pig"."""

import math
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


def simuliere_strategie(max_wuerfe, ziel_punkte, anzahl_spiele):
    """Simuliere mehrere Spiele.

    Eingabeparameter:
    - max_wuerfe: Anzahl der Würfe pro Runde
    - `max_wuerfe`: Maximale Anzahl der Würfe pro Runde
    - `ziel_punkte`: Anzahl der Punkte, die zum Sieg erreicht werden
      müssen.
    - `anzahl_spiele`: Anzahl der Spiele, die simuliert werden sollen.

    Rückgabe: Liste der Rundenanzahlen aller Spiele.
    """
    runden_liste = []
    for _ in range(anzahl_spiele):
        runden = spiele_strategie(max_wuerfe, ziel_punkte)
        runden_liste.append(runden)
    return runden_liste


def analysiere_strategie(runden_liste, strategie_name):
    mean = sum(runden_liste) / len(runden_liste)
    minimum = min(runden_liste)
    maximum = max(runden_liste)

    abweichungsquadratsumme = 0
    for runde in runden_liste:
        abweichungsquadratsumme += (runde - mean) ** 2

    standard_deviation = math.sqrt(abweichungsquadratsumme / len(runden_liste))

    print(
        f"""Strategie: {strategie_name}
Durchschnitt: {mean} Runden
Min: {minimum} Runden, Max: {maximum} Runden
Standardabweichung: {standard_deviation:.2f}"""
    )
