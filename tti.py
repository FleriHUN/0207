file=open("adatok.txt","r")















next(file)
#1.
print(len(file.readlines()),"ember adatait tartalmazza")
#3.
otvenalatt=0
for i in range(len(file)):
    if [i][2]<50:
        otvenalatt+=1
print(otvenalatt)

#6.
ttiindex=open("index.txt","w")
for i in file:
    if([i][1]==18 or 25):
        print("normális")
