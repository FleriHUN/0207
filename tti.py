<<<<<<< HEAD
file=open("adatok.txt","r")

next(file)
#1.
print(len(file.readlines()),"ember adatait tartalmazza")
#6.
ttiindex=open("index.txt","w")
for i in file:
    if([i][1]==18 or 25):
        print("normális")
=======
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
>>>>>>> 16f200e7033d3259e29b53f129cc00b79775d774
