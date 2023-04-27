from math import pi

print("A - Pc walca  B - Pc stożka  C - Pc kuli  D - V walca  E - V stożka  F - V kuli")
pnt=input().upper()

if pnt == "A":
    r = float(input("r="))
    H = float(input("H="))
    print(f"Pc = {2*pi*r**2+2*pi*r*H}")
elif pnt == "B":
    r = float(input("r="))
    l = float(input("l="))
    print(f"Pc = {pi*r**2+pi*r*l}")
elif pnt == "C":
    r = float(input("r="))
    print(f"Pc = {4*pi*r**2}")
elif pnt == "D":
    r = float(input("r="))
    H = float(input("H="))
    print(f"V = {pi*r**2*H}")
elif pnt == "E":
    r = float(input("r="))
    H = float(input("H="))
    print(f"V = {1/3*pi*r**2*H}")
elif pnt == "F":
    r = float(input("r="))
    print(f"V = {3/4*pi*r**3}")
else:
    print("hixsfiaf")