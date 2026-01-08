"""Übungsaufgabe: Timer

Erstelle eine Klasse Timer:

    Konstruktor: Initialisiert startzeit und laufend (None bzw. False)
    start(): Startet Timer (speichert time.time())
    stop(): Stoppt Timer
    vergangene_zeit(): Gibt Zeit in Sekunden zurück
    __str__(): Status ("läuft" oder "gestoppt: X.XX s")

t = Timer()
t.start()
# ... Code ausführen ...
t.stop()
print(t.vergangene_zeit())  # z.B. 2.34
"""

import time


class Timer:
    """Klasse, die einen Timer repräsentiert."""

    def __init__(self):
        """Initialisiert den Timer."""
        self.startzeit = None
        self.stoppzeit = None
        self.laufend = False

    def start(self):
        """Starte den Timer."""
        self.startzeit = time.time()
        self.laufend = True
    
    def stop(self):
        """Stoppe den Timer."""
        self.stoppzeit = time.time()
        self.laufend = False

    def vergangene_zeit(self):
        """Gibt die vergange Zeit zurück."""
        if self.startzeit is None:
            return 0
        if self.stoppzeit is None:
            aktuelle_zeit = time.time()
            return aktuelle_zeit - self.startzeit
        return self.stoppzeit - self.startzeit

    def __str__(self):
        """Gibt die Stringdarstellung des Timers zurück."""
        if self.laufend:
            return f"Läuft. Bisher vergangene Zeit: {self.vergangene_zeit():.2f} s"
        if self.startzeit is None:
            return "Noch nicht gestartet"
        return f"Gestoppt. Laufzeit {self.vergangene_zeit():.2f} s"
    

if __name__ == "__main__":
    timer1 = Timer()
    print(timer1)
    timer1.start()
    time.sleep(0.3)
    print(timer1)
    time.sleep(0.4)
    print(timer1)
    timer1.stop()
    print(timer1)
