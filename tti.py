file=open("adatok.txt", "r")

next(file)

#1. feladat
print(len(file.readlines()),"ember adatait tartalmazza")



magassagok=[]
for sor in file:
    adatok=sor.strip().split("\t")
    magassag=int(adatok[1])
    magassagok.append(magassag)



#2. feladat

atlagmag=sum(magassagok)/len(magassagok)
atlagmag=round(atlagmag,2)
print("Az átlagmagasság: ", atlagmag, "cm")


#3. feladat
otvenalatt=0
for i in range(len(file)):
    if [i][2]<50:
        otvenalatt+=1
print(otvenalatt)


#4. feladat

