# Zadanie 2

print("***************KALKULATOR***************")
a = input("Podaj pierwszą liczbę: ")
b = input("Podaj druga liczbę: ")
op = input("Podaj działanie: ")

# sprawdzenie czy a i b są liczbami
while a.replace('.', '', 1).isdigit() is False or b.replace('.', '', 1).isdigit() is False:
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

if op == "+":
    wynik = a + b
elif op == "-":
    wynik = a - b
elif op == "*":
    wynik = a * b
elif op == "/":
    if b == 0:
        wynik = "Nie można dzielić przez 0!"
    else:
        wynik = a / b
elif op == "//":
    if b == 0:
        wynik = "Nie można dzielić przez 0!"
    else:
        wynik = a // b
elif op == "**":
    wynik = a ** b
elif op == "%":
    wynik = a % b
else:
    wynik = "Wystapił błąd"

if str(wynik).replace('.', '', 1).isdigit():
    print("Wynik: ", float(wynik))
else:
    print(wynik)
