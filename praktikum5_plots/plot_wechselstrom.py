"""Visualisierung von Strom und Spannung an Wechselstromwiderständen.

u(t) = U0 sin(ωt)
i(t) = I0 sin(ωt+φ)
"""

import math
import matplotlib.pyplot as plt


# Konstanten

SPANNUNG0 = 325  # V
STROM0 = 23  # A
FREQUENZ = 50  # Hz
KREISFREQUENZ = 2 * math.pi * FREQUENZ


def spannung(t):
    """Spannung als Funktion der Zeit."""
    return SPANNUNG0 * math.sin(KREISFREQUENZ * t)


def strom(t, phi):
    """Spannung als Funktion der Zeit und Phasenverschiebung."""
    return STROM0 * math.sin(KREISFREQUENZ * t + phi)


if __name__ == "__main__":

    t_werte = [i * 0.04 / 200 for i in range(201)]

    # Ohm'scher Widerstand
    phi = 0
    u_werte = [spannung(ti) for ti in t_werte]
    i_werte = [strom(ti, phi) for ti in t_werte]
    plt.plot(t_werte, u_werte, "r-")
    plt.plot(t_werte, i_werte, "b--")
    plt.grid(True)
    plt.xlabel("Zeit / s")
    plt.ylabel("Spannung / V, Strom / A")
    plt.title("Ohm'scher Widerstand")
    plt.show()

    # Spule
    phi = -math.pi / 2
    u_werte = [spannung(ti) for ti in t_werte]
    i_werte = [strom(ti, phi) for ti in t_werte]
    plt.plot(t_werte, u_werte, "r-")
    plt.plot(t_werte, i_werte, "g:")
    plt.plot([0.005], [spannung(0.005)], "ro")
    plt.grid(True)
    plt.xlabel("Zeit / s")
    plt.ylabel("Spannung / V, Strom / A")
    plt.title("Spule")
    plt.show()

    # Kondensator
    phi = math.pi / 2
    u_werte = [spannung(ti) for ti in t_werte]
    i_werte = [strom(ti, phi) for ti in t_werte]
    plt.plot(t_werte, u_werte, "r-")
    plt.plot(t_werte, i_werte, color="orange")
    plt.plot([0.01], [strom(0.01, phi)], "ks")
    plt.grid(True)
    plt.xlabel("Zeit / s")
    plt.ylabel("Spannung / V, Strom / A")
    plt.title("Kondensator")
    plt.show()
