from copy import copy
from random import randint
# 1.Upewnij się czy dobrze rozumiesz jak działa kopiowanie obiektów.. np lst. 
# Jeśli masz wątpliwości wróć tam i siedź tam aż załapiesz co tam się dzieje!!!

a = [1, 2, 3]
b = copy(a)
b.append(4)
b.append(5)
print(a)
print(b)

# 2.Funkcję która może przyjąć nieskończenie wiele argumentów a następnie zwraca średnią arytmetyczną.

def funkcja(*argument):
    sum = 0
    for i in argument:
        sum += i
    srednia = sum/len(argument)
    return(srednia)
print(funkcja(1,2,3,4))

# 3.Funkcję która może przyjąć nieskończenie wiele argumentów a następnie zwraca średnią harmoniczną .

def funkcja_2(*argument):
    licznik = len(argument)
    mianownik = 0
    x = 0
    while licznik+1 >= x:
        mianownik += 1/argument[x]
        x += 1 
    śr_har = licznik/mianownik
    return(śr_har)
print(funkcja_2(1,2,3,4))

# 4.Funkcję która zamieni 2 wartości x i y. Zakładając że  x i y występują poza funkcją (Global).

def zamiana(x, y):
    x,y = y,x
    print(f"x = {x} y = {y}")
zamiana(1,2)

# 5.Wygeneruj 3 listy korzystając z nowo poznanej metody. (sam wymyśl parametry).

lista_1 = [randint(1, 10) for i in range(10)]
lista_2 = [i for i in range(15) if i % 2 == 0]
lista_3 = [i for i in range(20) if i >10 and i % 5 != 0]
print(lista_1)
print(lista_2)
print(lista_3)
