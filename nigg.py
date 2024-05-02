helyezes = []
csapat_meret = []
sportag = []
versenyszam = []
f = open("helsinki.txt", "r")
for x in f:
    szam = 0
    for sor in x.split():
        if(szam == 0):
            helyezes.append(sor)
        elif(szam == 1):
            csapat_meret.append(sor)
        elif(szam == 2):
            sportag.append(sor)
        else:
            versenyszam.append(sor)
        szam += 1

for x in range(len(helyezes)):
    print(helyezes[x])
    print(csapat_meret[x])
    print(sportag[x])
    print(versenyszam[x])
    print("")