"""Skript, das die Gleitstrecke eines Segelflugzeugs berechnet."""


def gleitstrecke_max(starthoehe_m, hoehenverlust_m_pro_km, hoehenreserve_m):
    """Berechnet die maximale Gleistrecke.

    Eingaben:
        - starthoehe_m: Starthöhe in Metern
        - hoehenverlust_m_pro_km: Höhenverlust in m/km
        - hoehenreserve_m: Höhenreserve am Ende des Flugs in m

    Ausgabe: Gleitstrecke in km
    """
    nutzbare_hoehe_m = starthoehe_m - hoehenreserve_m
    gleitstrecke_km = nutzbare_hoehe_m / hoehenverlust_m_pro_km
    return gleitstrecke_km


def ausgabe_gleistrecke(gleitstrecke_km):
    """Gibt die Gleitstrecke formatiert aus."""
    print(f"Die maximale Gleitstrecke beträgt {gleitstrecke_km:.2f} km.")


def main():
    starthoehe_m = float(input("Starthöhe in m: "))
    hoehenverlust_m_pro_km = float(input("Höhenverlust in m/km: "))
    hoehenreserve_m = float(input("Höhenreserve in m: "))
    gleitstrecke_km = gleitstrecke_max(
        starthoehe_m, hoehenverlust_m_pro_km, hoehenreserve_m
    )
    ausgabe_gleistrecke(gleitstrecke_km)


# siehe https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":  
    main()
