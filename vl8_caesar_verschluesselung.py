"""Cäsar-Verschlüsselung und -Entschlüsselung zur Demonstration von Stringmanipulation."""


def caesar_verschluesseln(text, verschiebung):
    """Verschlüssle einen Text mittels Cäsar-Chiffre"""
    original_text = text.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ergebnis = ""
    for zeichen in original_text:
        position = alphabet.find(zeichen)
        if position < 0:
            ergebnis += zeichen
        else:
            position += verschiebung
            position = position % 26
            neues_zeichen = alphabet[position]
            ergebnis += neues_zeichen
    return ergebnis


def caesar_entschluesseln(text, verschiebung):
    """Entschlüssle einen Cäsar-verschlüsselten Text."""
    return caesar_verschluesseln(text, -verschiebung)


if __name__ == "__main__":
    cypher_text = caesar_verschluesseln("HALLO WELT!", 3)
    print(cypher_text)
    for i in range(1, 25):
        print(caesar_entschluesseln(cypher_text, i))
