from Kostka import Kostka
from Zdravic import Zdravic

zdravic = Zdravic()
zdravic.text = "Ahoj"
print(zdravic.pozdrav("hráči!"))

sestistenna_kostka = Kostka()
desetistenna_kostka = Kostka(10)

print(sestistenna_kostka)
for _ in range(10):
    print(sestistenna_kostka.hod_kostkou(), end=" ")

print("\n", desetistenna_kostka, sep="")
for _ in range(10):
    print(desetistenna_kostka.hod_kostkou(), end=" ")
