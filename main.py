import random

def frågor():
    return [
        # Polynom
        ("Vad är derivatan av x^2?", "2x"),
        ("Vad är derivatan av x^3?", "3x^2"),
        ("Vad är derivatan av 5x?", "5"),
        ("Vad är derivatan av 7?", "0"),
        ("Vad är derivatan av 3x^2?", "6x"),

        # Exponentialfunktioner
        ("Vad är derivatan av e^x?", "e^x"),
        ("Vad är derivatan av e^(2x)?", "2e^(2x)"),
        ("Vad är derivatan av 2^x?", "ln(2)*2^x"),
        ("Vad är derivatan av 5^x?", "ln(5)*5^x"),

        # Blandade uttryck
        ("Vad är derivatan av x^2 + 3e^x + 2e^(2x)?", "2x+3e^x+4e^(2x)"),
        ("Vad är derivatan av x^3 + 2x + 2e^x + 3e^(2x)?", "3x^2+2+2e^x+6e^(2x)"),
        ("Vad är derivatan av 4x^2 + x + 3e^x + e^(3x)?", "8x+1+3e^x+3e^(3x)"),
        ("Vad är derivatan av x^2 + 2x + e^x + 2e^(2x)?", "2x+2+e^x+4e^(2x)"),

        # Blandade med luringar
        ("Vad är derivatan av x^2 + 2e^x + 3e^(2x) + pi?", "2x+2e^x+6e^(2x)"),
        ("Vad är derivatan av x^3 + 2x + e + 2e^x + e^(2x)?", "3x^2+2+2e^x+2e^(2x)"),
        ("Vad är derivatan av 3x^2 + e^x + 2e^(3x) + 4pi?", "6x+e^x+6e^(3x)"),
        ("Vad är derivatan av x^2 + 2^x + 2e^x + 3e^(2x) + e?", "2x+ln(2)*2^x+2e^x+6e^(2x)"),

        # Blandade med nämnare
        ("Vad är derivatan av 1/x + x + e^x?", "-1/x^2+1+e^x"),
        ("Vad är derivatan av 1/x^2 + x^2 + 2e^(2x)?", "-2/x^3+2x+4e^(2x)"),
        ("Vad är derivatan av 2/x + 3x + e^x + e^(2x)?", "-2/x^2+3+e^x+2e^(2x)"),
        ("Vad är derivatan av 3/x^2 + x^3 + 2e^x?", "-6/x^3+3x^2+2e^x"),
        ("Vad är derivatan av 1/x^3 + 2x^2 + e^x + e^(2x)?", "-3/x^4+4x+e^x+2e^(2x)"),
        ("Vad är derivatan av 4/x + x^2 + 2^x + 2e^x?", "-4/x^2+2x+ln(2)*2^x+2e^x"),

        # Endast nämnare
        ("Vad är derivatan av 1/x?", "-1/x^2"),
        ("Vad är derivatan av 1/x^2?", "-2/x^3"),
        ("Vad är derivatan av 1/x^3?", "-3/x^4"),
        ("Vad är derivatan av 2/x?", "-2/x^2"),
        ("Vad är derivatan av 5/x^2?", "-10/x^3"),
        ("Vad är derivatan av 3/x^4?", "-12/x^5"),
        ("Vad är derivatan av 7/x^3?", "-21/x^4")
    ]


def kör_test():
    alla_frågor = frågor()
    random.shuffle(alla_frågor)

    poäng = 0
    antal_frågor = 10  # ändra om du vill ha fler/färre frågor

    print("=== Deriveringstest ===\n")

    for i in range(antal_frågor):
        fråga, svar = alla_frågor[i]

        print(f"Fråga {i+1}: {fråga}")
        elev_svar = input("Ditt svar: ").replace(" ", "")

        if elev_svar.lower() == svar.lower():
            print("Rätt!\n")
            poäng += 1
        else:
            print(f"Fel. Rätt svar är: {svar}\n")

    print(f"Resultat: {poäng} av {antal_frågor} rätt!")


if __name__ == "__main__":
    kör_test()

