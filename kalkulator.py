# Zadanie 2

print("***************KALKULATOR***************")
a = input("Podaj pierwszą liczbę: ")
b = input("Podaj druga liczbę: ")
op = input("Podaj działanie: ")

# sprawdzenie czy a i b są liczbami
while a.isdigit() is False or b.isdigit() is False:
    print("Proszę podać prawidłową liczbę!")
    a = input("Podaj pierwszą liczbę: ")
    b = input("Podaj druga liczbę: ")
    op = input("Podaj działanie: ")

# sprawdzenie czy zostala wpisana poprawna operacja
while op not in {"+", "-", "*", "/", "//", "**", "%"}:
    print("Proszę podać prawidłowy operator!")
    a = input("Podaj pierwszą liczbę: ")
    b = input("Podaj druga liczbę: ")
    op = input("Podaj działanie: ")

# zamiana napisow na liczby
a = float(a)
b = float(b)
if (op == "/" or op == "//") and b == 0:
    wynik = "Nie można dzielić przez 0!"

else:
    if op == "+":
        wynik = a + b
    elif op == "-":
        wynik = a - b
    elif op == "*":
        wynik = a * b
    elif op == "/":
        wynik = a / b
    elif op == "//":
        wynik = a // b
    elif op == "**":
        wynik = a ** b
    elif op == "%":
        wynik = a % b
    else:
        wynik = "Wystapił błąd"

print("Wynik: " + str(round(wynik)))
