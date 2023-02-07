file=open("adatok.txt", "r")

next(file)





































#2. feladat

magassagok=[]
for sor in file:
    adatok=sor.strip().split("\t")
    magassag=int(adatok[1])
    magassagok.append(magassag)

file.close()

atlagmag=sum(magassagok)/len(magassagok)
atlagmag=round(atlagmag,2)
print("Az átlagmagasság: ", atlagmag, "cm")