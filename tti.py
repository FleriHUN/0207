file=open("adatok.txt","r")

next(file)
#1.
print(len(file.readlines()),"ember adatait tartalmazza")
#6.
ttiindex=open("index.txt","w")
for i in file:
    if([i][1]==18 or 25):
        print("normális")
