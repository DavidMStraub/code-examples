"""Zusatzaufgabe: Nullstellen markieren

Plotten Sie die Funktion f(x)=x²-4 für x-Werte von -3 bis 3.

Aufgaben:

    Plotten Sie die Funktion als blaue durchgezogene Linie
    Markieren Sie die beiden Nullstellen (x=-2 und 2) als große rote Punkte
    Fügen Sie eine Legende hinzu
    Vergessen Sie nicht Titel, Achsenbeschriftungen und Gitter
"""

import matplotlib.pyplot as plt


def f(x):
    return x**2 - 4


if __name__ == "__main__":

    x = [i / 100 * 6 - 3 for i in range(101)]
    y = [f(xi) for xi in x]
    x_nullstellen = [-2, 2]
    y_nullstellen = [0 for _ in x_nullstellen]

    plt.plot(x, y, "b-", label="Funktion")
    plt.plot(x_nullstellen, y_nullstellen, "ro", label="Nullstellen")
    plt.title("x² - 4 und Nullstellen")
    plt.xlabel("x")
    plt.ylabel("f")
    plt.grid(True)
    plt.legend()
    plt.show()