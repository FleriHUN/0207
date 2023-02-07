file=open("adatok.txt", "r")

next(file)

magassagok=[]
for sor in file:
    adatok=sor.strip().split("\t")
    magassag=int(adatok[1])
    magassagok.append(magassag)

file.close()

#1. feladat















#2. feladat



atlagmag=sum(magassagok)/len(magassagok)
atlagmag=round(atlagmag,2)
print("Az átlagmagasság: ", atlagmag, "cm")

#3. feladat


















#4.


