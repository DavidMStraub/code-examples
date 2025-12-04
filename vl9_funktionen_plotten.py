"""Aufgabe: Funktionen visualisieren

Erstellen Sie einen Plot mit drei mathematischen Funktionen für x-Werte von 0 bis 10.

Funktionen:

- Linear: f(x) = 2x
- Quadratisch: g(x)=x²
- Kubisch: h(x)=0.1x³

Anforderungen:
    Verwenden Sie List Comprehensions für die y-Werte
    Verschiedene Farben und Linien-Stile
    Titel und Achsenbeschriftungen
    Gitter aktivieren
"""

import matplotlib.pyplot as plt


def f(x):
    """Lineare Funktion."""
    return 2 * x


def g(x):
    """Quadratische Funktion."""
    return x**2


def h(x):
    """Kubische Funktion."""
    return 0.1 * x**3


if __name__ == "__main__":

    x = [i * 0.1 for i in range(101)]
    y_f = [f(xi) for xi in x]
    y_g = [g(xi) for xi in x]
    y_h = [h(xi) for xi in x]

    plt.plot(x, y_f, "r-")
    plt.plot(x, y_g, "b--")
    plt.plot(x, y_h, "k:")
    plt.title("Libeare, quadratische und kubische Funktion")
    plt.xlabel("x")
    plt.ylabel("f(x), g(x), h(x)")
    plt.grid(True)
    plt.show()
