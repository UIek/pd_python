import funkcje
from math import pi 

inp = input("a-V szescianu , b-Pc szescianu , c-V prostopadloscian , d-Pc prostopadloscian ,e-V_graniastoslup ......... ")

if inp == "a":
    funkcje.V_szescianu()
if inp == "b":
    funkcje.Pc_szescianu()
if inp == "c":
    a = float(input("a="))
    b = float(input("b="))
    funkcje.V_prostopadloscian(a,b)
if inp == "d":
    funkcje.Pc_prostopadloscian()
if inp == "e":
    Pb = float(input("Pb="))
    H = float(input("H="))
    funkcje.V_graniastoslup(Pb,H)
    print(Pb*H)
if inp == "f":
    funkcje.V_kuli()
if inp == "g":
    r = float(input("r="))
    funkcje.Pc_kuli(r)
    print(4*pi*r**2)
if inp == "h":
    funkcje.V_stozka()
if inp == "i":
    r = float(input("r="))
    funkcje.Pc_stozka(r)
if inp == "j":
    funkcje.V_walca()
if inp == "k":
    funkcje.Pc_walca()
if inp == "l":
    h = float(input("h="))
    funkcje.V_ostroslupa(h)
if inp == "m":
    funkcje.Pc_ostroslupa()
if inp == "n":
    r = float(input("r="))
    funkcje.pole_kola(r)
    print(pi*r**2)
if inp == "o":
    funkcje.pole_kwadratu()
if inp == "p":
    funkcje.pole_prostokata()
if inp == "r":
    e = float(input("e="))
    f = float(input("f="))
    funkcje.pole_rabu(e,f)
    print(e*f/2)
if inp == "s":
    funkcje.pole_prostopadloscianu()
if inp == "t":
    funkcje.pole_trapezu()
if inp == "u":
    Pb = float(input("Pb="))
    Pp = float(input("Pp="))
    funkcje.Pc_graniastoslup(Pb,Pp)
    print(Pb+Pp*2)
