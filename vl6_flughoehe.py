"""Skript um die Flughöhe einer Raktete zu bestimmen."""

import math
import random


def berechne_flughoehe(startgeschwindigkeit, startwinkel_grad, flugzeit):
    """Berechne die Flughöhe `flugzeit` Sekunden.

    Eingabeparameter:
    - startgeschwindigkeit: Startgeschwindigkeit in m/s
    - startwinkel_grad: Startwinkel in Grad
    - flugzeit: Flugzeit in s
    """
    startwinkel = math.radians(startwinkel_grad)
    return startgeschwindigkeit * flugzeit * math.sin(startwinkel)


if __name__ == "__main__":

    for i in range(5):
        random.seed(i)

        v0 = random.random() * 1000 + 7500
        alpha_grad = random.random() * 5 + 85

        flughoehe = berechne_flughoehe(v0, alpha_grad, 10)

        print(
            f"""Startgeschwindigkeit: {v0:.1f} m/s,
Startwinkel: {alpha_grad:.2f}°,
Flughöhe nach 10 s: {flughoehe:.2f} m
"""
        )
