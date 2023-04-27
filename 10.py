from time import sleep
from random import randint
from copy import copy
# 1.Napisz “Timer” przyjmuje od użytkownika liczbę minut. Liczymy za ile skończy się czas.

min = float(input("wprowaź liczbę minut..."))
sec = float(input("wprowaź liczbe sekund..."))
czas = min*60 + sec
i = 1

while i <= sec:
    sleep(1)
    print(i)
    i += 1

print("czas minoł")

# 2.Stwórz krotkę/tuples zawierającą 6 elementów. 
# Zmień ją na listę, usuń 2 ostatnie elementy i zmień z powrotem na krotkę.

xyz = (1, 2, 3, 4, 5, 6)
xyz = list(xyz)
xyz.pop(-1)
xyz.pop(-1)
xyz = tuple(xyz)
print(xyz)

# 3.Napisz funkcję zwracającą krotki/tuples(10/20 elementów) o losowych 
# wartościach z przedziału 1,10. Następnie napisz 2 funkcję która
# przyjmie naszą krotkę jako argument, pozbędzie się duplikatów,
# posortuje (od największej wartości do najmniejszej!) i zwraca krotkę 

def tuples():
    tuple_1  = [randint(1, 10) for el in range(15)]
    tuple_1 = tuple(tuple_1)
    return(tuple_1)
tuples()

def brak_duplik(tuple_1):
    tuple_1 = set(tuple_1)
    tuple_1 = list(tuple_1)
    tuple_1.sort(reverse = True)
    tuple_1 = tuple(tuple_1)
    return(tuple_1)
brak_duplik(tuples())

#4.Napisz funkcję która przepisze listę  moja lista na krotkę. 

moja_lista = [randint(1,20) for i in range(20)]
def krotka(moja_lista):
    moja_lista = tuple(moja_lista)
    return(moja_lista)
krotka(moja_lista)

# 5.Napisz funkcję która sprawdza czy zapytany element jest w set.

klasa_1c = {"Ala","Maciek","Kasia", "Olek", "Basia", "Wojtek"}

def Aaaaaa(klasa_1c):
    inp = input("wpisz coś...")
    klasa_1c = list(klasa_1c)
    klasa_1c.append(inp)
    klasa_1c_2 = copy(klasa_1c) 
    klasa_1c_2 = set(klasa_1c_2)
    if len(klasa_1c) == len(klasa_1c_2):
        print("tego elementu nie ma w zbiorze")
    else:
        print('ten element jest w już w zbiorze')
Aaaaaa(klasa_1c)
    



