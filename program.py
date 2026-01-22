import re
import pyperclip # pakiet do kopiowania komendy do schowka do zainstalowania


while True:
    print("Wklej koordynaty: ")
    bufor = []

    for _ in range(2):
        linia = input()
        bufor.append(linia)

    tekst = "\n".join(bufor)

    liczby = re.findall(r'-?\d+\.\d+', tekst)

    if len(liczby) >= 2:
        wynik = f"/tpll {liczby[0]}, {liczby[1]}"
        pyperclip.copy(wynik)
        print("Skopiowano do schowka: ",wynik)
    else:
        print("Nie znaleziono dwóch współrzędnych.")
