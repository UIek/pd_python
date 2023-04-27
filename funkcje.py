from math import pi

def V_szescianu():
    a = float(input("a="))
    print(a**3)

def Pc_szescianu():
    a = float(input("a="))
    print(a**2*6)

def V_prostopadloscian(a,b):
    h = float(input("h="))
    print(a*b*h)

def Pc_prostopadloscian():
    Pb = float(input("Pb="))
    Pp = float(input("Pp="))
    print(Pb+2*Pp)

def V_graniastoslup(Pb,H):
    return(Pb*H)

def Pc_graniastoslup(Pb,Pp):
    return(Pb+Pp*2)

def V_kuli():
    r = float(input("r="))
    print(3/4*pi*r**3)

def Pc_kuli(r):
    return(4*pi*r**2)

def V_stozka():
    r = float(input("r="))
    H = float(input("H="))
    print(1/3*pi*r**2*H)

def Pc_stozka(r):
    l = float(input("l="))
    print(pi*r**2+pi*r*l)

def V_walca():
    r = float(input("r="))
    H = float(input("H="))
    print(pi*r**2*H)

def Pc_walca():
    r = float(input("r="))
    H = float(input("H="))
    print(2*pi*r**2+2*pi*r*H)

def V_ostroslupa(h):
    Pp = float(input("Pp="))
    print(1/3*Pp*h)

def Pc_ostroslupa():
    Pp = float(input("Pp="))
    Pb = float(input("Pb="))
    print(Pp+Pb)

def pole_kola(r):
    return(pi*r**2)

def pole_kwadratu():
    a = float(input("a="))
    print(a**2)

def pole_prostokata():
    a = float(input("a="))
    b = float(input("b="))
    print(a*b)

def pole_rabu(e,f):
    return(e*f/2)

def pole_prostopadloscianu():
    a = float(input("a="))
    h = float(input("h="))
    print(a*h)

def pole_trapezu():
    a = float(input("a="))
    b = float(input("b="))
    h = float(input("h="))
    print((a+b)*h/2)





