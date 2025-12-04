import matplotlib.pyplot as plt
import numpy as np


def spannung(t):
    """Berechnet die Spannung zu einem gegebenen Zeitpunkt t.

    Die Amplitude und Frequenz sind als 1 definiert.
    """
    omega = 2 * np.pi
    return np.cos(omega * t)


def strom(t, phi):
    """Berechnet den Strom zu einem gegebenen Zeitpunkt t mit Phasenverschiebung phi.

    Die Amplitude und Frequenz sind als 1 definiert.
    """
    omega = 2 * np.pi
    return np.cos(omega * t - phi)


def leistung(t, phi):
    """Berechnet die Leistung zu einem gegebenen Zeitpunkt t mit Phasenverschiebung phi."""
    return spannung(t) * strom(t, phi)


def wirkleistung(t, phi):
    """Berechnet die zeitabhängige Wirkleistungskomponente.

    Verwendet: cos(a)*cos(b) = 1/2[cos(a-b) + cos(a+b)]
    Dies ist der Teil mit dem Mittelwert cos(phi)/2.
    """
    omega = 2 * np.pi
    return 0.5 * np.cos(phi) * (1 + np.cos(2 * omega * t))


def blindleistung(t, phi):
    """Berechnet die zeitabhängige Blindleistungskomponente.

    Dies ist der Teil mit verschwindendem Mittelwert.
    """
    omega = 2 * np.pi
    return 0.5 * np.sin(phi) * np.sin(2 * omega * t)


def plot_scheinleistung(phi, ax=None):
    """Erstellt ein Plot der Spannung, des Stroms und der Leistungskomponenten."""

    if ax is None:
        fig, ax = plt.subplots(3, 1, figsize=(8, 8))
    
    t = np.linspace(0, 1, 1000)

    u = spannung(t)
    i = strom(t, phi)
    p = leistung(t, phi)
    pw = wirkleistung(t, phi)
    pb = blindleistung(t, phi)

    ax[0].cla()
    ax[0].axhline(y=0, color="black", linewidth=0.8)
    ax[0].plot(t, u, label="$u(t)$", color="C0")
    ax[0].plot(t, i, label="$i(t)$", color="C1", linestyle="--")
    ax[0].set_ylim(-1.1, 1.1)
    ax[0].set_title("Spannung und Strom")
    ax[0].set_xlabel("$t$ / s")
    ax[0].set_ylabel("Amplitude")
    ax[0].legend()

    ax[1].cla()
    ax[1].axhline(y=0, color="black", linewidth=0.8)
    ax[1].plot(t, p, label="$p(t)=p_w(t)+q(t)$", color="C2")
    ax[1].axhline(y=0.5 * np.cos(phi), color="C2", linestyle="--", label="$P$")
    ax[1].set_ylim(-0.6, 1.1)
    ax[1].set_title("Momentanleistung")
    ax[1].set_xlabel("$t$ / s")
    ax[1].set_ylabel("Leistung")
    ax[1].legend()

    ax[2].cla()
    ax[2].axhline(y=0, color="black", linewidth=0.8)
    ax[2].plot(t, pw, label="$p_w(t)$", color="C3")
    ax[2].plot(t, pb, label="$q(t)$", color="C4", linestyle="--")
    ax[2].set_ylim(-0.6, 1.1)
    ax[2].set_title("Wirkleistung und Blindleistung")
    ax[2].set_xlabel("$t$ / s")
    ax[2].set_ylabel("Leistung")
    ax[2].legend()

    plt.tight_layout()
    return ax