# Zadanie 3
# pytanie: opdowiedź:  -> na końcu robimy "raport"

pytanie0 = "Jak masz na imię oraz nazwisko?"
pytanie1 = "Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:"
pytanie2 = "W jakich okolicznościach czytasz książki najczęściej?"
pytanie3 = "Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?"
pytanie4 = "Po książki w jakiej formie sięgasz najczęściej?"
pytanie5 = "Ile książek czytasz średnio w ciągu roku?"
pytanie6 = "Jak często średnio czytasz książki?"
pytanie7 = "Po jakie gatunki książek sięgasz najczęściej?"

pytania = [pytanie1, pytanie2, pytanie3, pytanie4, pytanie5, pytanie6, pytanie7]

zestaw1 = {"1": "ogladanie telewizji/filmów/seriali",
           "2": "czytanie książek/czasopism",
           "3": "słuchanie muzyki",
           "4": "spotkania z rodziną/przyjaciółmi",
           "5": "podróżowanie",
           "6": "uprawianie sportu",
           "7": "inne"}

zestaw2 = {"1": "podczas podróży",
           "2": "w czasie wolnym (po pracy, na urlopie)",
           "3": "podczas pracy/nauki (to ich element)",
           "4": "w ogóle nie czytam",
           "5": "inne"}

zestaw3 = {"1": "chęć poszerzenia wiedzy",
           "2": "czytanie mnie relaksuje/odpręża",
           "3": "fakt, że czytanie jest modne",
           "4": "czytanie to moje hobby",
           "5": "konieczność nauki w związku z wykonywaną pracą/studiami",
           "6": "odczuwam presję rodziny/środowiska, żeby czytać",
           "7": "inny"}

zestaw4 = {"1": "papierowej (tradycyjnej)",
           "2": "e-booki (książki elektroniczne) na komputerze",
           "3": "e-booki na tablecie/telefonie",
           "4": "e-booki na specjalnym czytniku (np. Kindle)"}

zestaw5 = {"1": "0",
           "2": "żadnej w całości - jedynie fragmenty",
           "3": "1",
           "4": "2 lub 3",
           "5": "4-10",
           "6": "powyżej 10"}

zestaw6 = {"1": "codziennie",
           "2": "raz w tygodniu",
           "3": "raz w miesiącu",
           "4": "raz na kilka miesięcy",
           "5": "raz na pół roku",
           "6": "raz na rok",
           "7": "wcale"}

zestaw7 = {"1": "kryminały/thrillery",
           "2": "romanse",
           "3": "psychologiczne",
           "4": "horrory",
           "5": "naukowe",
           "6": "dla dzieci i młodzieży",
           "7": "fantastykę",
           "8": "biograficzne",
           "9": "historyczne",
           "10": "science fiction",
           "11": "podróżnicze",
           "12": "hobbystyczne (gotowanie, wędkarstwo itp.)",
           "13": "przygodowe",
           "14": "poezję",
           "15": "inne"}

zestawy = [zestaw1, zestaw2, zestaw3, zestaw4, zestaw5, zestaw6, zestaw7]
odpowiedzi = []

# Ankieta
print("****************ANKIETA******************")
odpowiedzi.append(input(pytanie0 + " "))

for i in range(7):
    print("Pytanie " + str(i+1) + ". " + pytania[i])
    for opcja in zestawy[i]:
        print(opcja, zestawy[i][opcja], sep=". ")
    odpowiedzi.append(input("Podaj numer: "))

# raport
print("\n****************RAPORT********************")
print("Pytanie: ", pytanie0, "\nOdpowiedź: ", odpowiedzi[0])
for i in range(7):
    print("Pytanie: ", pytania[i], "\nOdpowiedź: ", end="")
    if odpowiedzi[i+1] in zestawy[i]:
        print(zestawy[i][odpowiedzi[i+1]])
    else:
        print("Podano błędnie odpowiedź")
