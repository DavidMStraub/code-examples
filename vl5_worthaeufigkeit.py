# EINGABE
text = "Python ist toll Python macht Spass toll toll"

# VERARBEITUNG
worte = text.split()

worthaeufigkeiten = {}

for wort in worte:
    if wort not in worthaeufigkeiten:
        worthaeufigkeiten[wort] = 1
    else:
        worthaeufigkeiten[wort] += 1

# AUSGABE
print(f"Häufigkeit der Worte: {worthaeufigkeiten}")
