"""Übungsaufgabe: Widerstand

Erstelle eine Klasse Widerstand:
    Konstruktor: Widerstandswert in Ohm
    parallel(self, r2): Ersatzwiderstand Parallelschaltung
    reihe(self, r2): Ersatzwiderstand Reihenschaltung
    leistung(self, spannung): Leistung
    __str__(): z.B. "100 Ω"

r1 = Widerstand(100)
print(r1.parallel(200))  # 66.67
print(r1.leistung(5))   # 0.25
"""

class Widerstand:
    """Klasse, die einen Ohm'schen Widerstand repräsentiert."""

    def __init__(self, wert_ohm):
        """Initialisiere den Widerstand mit einem Wert in Ohm."""
        self.wert_ohm = wert_ohm

    def __str__(self):
        """Stelle die Instanz als String dar."""
        return f"{self.wert_ohm:.0f} Ω"
    
    def reihe(self, r2):
        """Berechne den Ersatzwiderstand bei Reihenschaltung mit r2."""
        r1 = self.wert_ohm
        return r1 + r2
    
    def parallel(self, r2):
        """Berechne den Ersatzwiderstand bei Parallelschaltung mit r2.
        
        Verwendet 1/R = 1/R1 + 1/R2
        """
        r1 = self.wert_ohm
        return 1 / (1 / r1 + 1 / r2)
    
    def leistung(self, spannung):
        """Berechne die Leistung P=U²/R für eine gegebene Spannung."""
        return spannung**2 / self.wert_ohm


if __name__ == "__main__":
    widerstand1 = Widerstand(100)
    print(widerstand1.leistung(5))

