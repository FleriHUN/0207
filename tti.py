file = open("adatok.txt", "r")

next(file)

#1. feladat
sorok=file.readlines()
print(len(sorok),"ember adatait tartalmazza")

#2. feladat

magassagok=[]
for sor in sorok:
    adatok=sor.strip().split("\t")
    magassag=int(adatok[1])
    magassagok.append(magassag)

atlagmag=sum(magassagok)/len(magassagok)
atlagmag=round(atlagmag, 2)
print("Az átlagmagasság: ", atlagmag, "cm")

#3. feladat
otvenalatt=0
for sor in sorok:
    adatok=sor.strip().split("\t")
    testsuly=int(adatok[2])
    if testsuly<50:
        otvenalatt+=1
print(otvenalatt, "fő testsúlya 50 kg alatt van.")

#4. feladat

minimum_magassag = int(input("Add meg a minimális magasságot (cm): "))
felelos=0
felelok=[]
for sor in sorok:
    adatok=sor.strip().split("\t")
    nev=adatok[0]
    magassag=int(adatok[1])
    if magassag>=minimum_magassag:
        felelos+=1
        felelok.append(nev)

print(felelos, "fő felel meg a kritériumnak.")
print("A megfelelő játékosok:", felelok)


#file.close()