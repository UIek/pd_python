class Uczen():
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    def umiePisac (self):
        print(f"{self.imie} umie pisać")
    def umieMowic (self):
        print(f"{self.imie} umie mówić")

class Prymus (Uczen):
    def nieSpi (self):
        print(f"{self.imie} nie śpi, tylko się uczy")
    def same6 (self):
        print(f"{self.imie} ma same 6")

class Pajac (Uczen):
    def wyglupy (self):
        print(f"{self.imie} ciągle się wygłupia")
    def robi_zarty (self):
        print(f"{self.imie} robi głupie żarty")

class Marzyciel (Uczen):
    def marzy (self):
        print(f"{self.imie} ciągle marzy")
    def spiNalekcjach (self):
        print(f"{self.imie} śpi na lekcjach")

class Sportowiec (Uczen):
    def pilkanozna (self):
        print(f"{self.imie} gra w piłkę nożną ")
    def zawody (self):
        print(f"{self.imie} bierze udział we wszystkich zawodach sportowych")

class Przecietny (Uczen):
    def zmieniabuty (self):
        print(f"{self.imie} zmienia buty")
    def grzeczny (self):
        print(f"{self.imie} nie gada na lekcjach")

class Wagarowicz (Uczen):
    def spoznienia (self):
        print(f"{self.imie} ciągle się spóźnia")
    def brakzainteresowania (self):
        print(f"{self.imie} nie obchodzi go szkoła")