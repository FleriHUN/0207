<<<<<<< HEAD
file=open("adatok.txt","r")

next(file)
#1.
for i in file:
    print(Ladatok.append([i](len)))
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
>>>>>>> 3d198bfe9f7b561458132d0906f19419bb3a6e5d
