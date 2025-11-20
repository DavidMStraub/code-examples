"""Simulation der optimalen Pig-Strategie."""

import pig_funktionen

if __name__ == "__main__":

    simulationen = {}
    for i in range(2, 10):
        simulationen[i] = pig_funktionen.simuliere_strategie(
            max_wuerfe=i, ziel_punkte=100, anzahl_spiele=1000
        )

        pig_funktionen.analysiere_strategie(simulationen[i], f"{i} Würfe")
        print("---")
