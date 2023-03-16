# Zadanie 1

napis1 = napis2 = napis3 = "Python 2023"

print("Porównanie napisu pierwszego i drugiego: " + str(napis1 == napis2))
print("Porównanie napisu drugiego i trzeciego: " + str(napis2 == napis3))

print("Typ: " + str(type(napis1)) + " Adres: " + str(hex(id(napis1))))
print("Typ: " + str(type(napis2)) + " Adres: " + str(hex(id(napis2))))
print("Typ: " + str(type(napis3)) + " Adres: " + str(hex(id(napis3))))

napis3 = "Java 11"
print("\nPo zmianie napisu trzeciego: ")

print("Porównanie napisu pierwszego i drugiego: " + str(napis1 == napis2))
print("Porównanie napisu drugiego i trzeciego: " + str(napis2 == napis3))

print("Typ: " + str(type(napis1)) + " Adres: " + str(hex(id(napis1))))
print("Typ: " + str(type(napis2)) + " Adres: " + str(hex(id(napis2))))
print("Typ: " + str(type(napis3)) + " Adres: " + str(hex(id(napis3))))
