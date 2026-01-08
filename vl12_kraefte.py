"""Beispielaufgabe: Kräftegleichgewicht

Drei Kräfte wirken auf einen Punkt.

Aufgaben: Berechne die resultierende Kraft 

Bestimme , sodass Gleichgewicht herrscht 
Berechne die Beträge aller Kräfte mit np.linalg.norm()
Berechne den Winkel zwischen F1 und F2"""

import math
import numpy as np

F1 = np.array([3.0, 4.0, 0.0])
F2 = np.array([-2.0, 1.0, 5.0])
Fres = F1 + F2

# Fres + F3 = 0
# F3 = -Fres
F3 = -Fres

F1_abs = np.linalg.norm(F1)
F2_abs = np.linalg.norm(F2)
F3_abs = np.linalg.norm(F3)

cos_alpha = np.dot(F1, F2) / (F1_abs * F2_abs)
alpha = math.acos(cos_alpha)
alpha_degrees = math.degrees(alpha)

print(alpha_degrees)
