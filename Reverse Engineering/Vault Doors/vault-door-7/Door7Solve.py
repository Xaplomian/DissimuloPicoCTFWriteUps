numbers = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734293602, 1701067056, 892756537]
binaries = []

for i in numbers:
    num = str(bin(i))[2::]
    binout = int(31 - int(len(num))) * '0' + num
    binaries.append(binout)
print(binaries)

madebinaries = []
for i in binaries:
    for j in range(8):
        temp = 
    templist = [int(i[0:7]), int(i[8:15]), int(i[16:24]), int(i[25:31])]
    madebinaries.append(templist)
    print(templist)
print(madebinaries)

for i in madebinaries:
    for j in i:
        j = str(j)
        output = int(8 - int(len(j))) * '0' + j
        print(output)
        print(chr(int(output, 2)))
                
input()