#2. feladat - Olvassa be a helsinki.txt állományban lévő adatokat és tárolja el egy olyan
#adatszerkezetben, amely a további feladatok megoldására alkalmas!

#Osztály létrehozása adatok tárolásához:
class Eredmeny:
    def __init__(self, helyezes, sportolokSzama, sportag, versenyszam):
        self.helyezes = helyezes
        self.sportolokSzama = sportolokSzama
        self.sportag = sportag
        self.versenyszam = versenyszam

# Fájl beolvasása és objektumok létrehozása, osztály segítségével:

def FileBeolvasas():
    Eredmenyek = []
    with open("helsinki.txt", "r", encoding="utf-8") as f:
        for sor in f:
            adatok = sor.strip().split(" ")
            helyezes = int(adatok[0])
            sportolokSzama = int(adatok[1])
            sportag = adatok[2]
            versenyszam = adatok[3]
            eredmeny = Eredmeny(helyezes, sportolokSzama, sportag, versenyszam)
            Eredmenyek.append(eredmeny)
    return Eredmenyek

#Adatok lekérdezése, függvény meghívásával
adatok=FileBeolvasas()

# Eredmény kiírása
def AdatKiiratas():
    for aktErdemeny in adatok:
        print(vars(aktErdemeny))

#Adatkiíró függvény meghívása
AdatKiiratas()

