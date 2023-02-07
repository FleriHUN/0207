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

#5. feladat

felelok.sort()
with open("abc.txt", "w",encoding="UTF-8") as file:
    for nev in felelok:
        file.write(nev+"\n")
file.close()

#6. feladat

testsulyok=[]
for sor in sorok:
    adatok=sor.strip().split("\t")
    testsuly=int(adatok[2])
    testsulyok.append(testsuly)

for i in range(len(sorok)):
    bmi = round(testsulyok[i]/(magassagok[i]/100)**2, 2)
    if bmi<18:
        testalkat="sovány"
    elif bmi<25:
        testalkat="normális"
    else:
        testalkat="túlsúlyos"
    with open("index.txt", "a", encoding="UTF-8") as file:
        file.write(sorok[i].strip().split("\t")[0]+ "\t" + str(bmi) + "\t" + testalkat + "\n")

file.close()
