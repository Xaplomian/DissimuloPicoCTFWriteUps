numbers = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734293602, 1701067056, 892756537]
binaries = []
final = ''

for i in numbers:
    num = str(bin(i))[2::]
    binout = int(32 - int(len(num))) * '0' + num
    binaries.append(binout)
print('Binaries')
print(binaries)

#for i in binaries:
#    for j in range(8):
#        i[j] = (i[j*4] >> 24) | (i[j*4+1] >> 16) | (i[j*4+2] >> 8) | (i[j*4+3])
#        print(str(i))

madebinaries = []
for i in binaries:
    for j in range(8):
        templist = [int((i[0:7]),2), int((i[8:15]),2), int((i[16:24]),2), int((i[25:31]),2)]
        templist[0] = templist[0]
        templist[1] = templist[1]
        templist[2] = templist[2]
        templist[3] = templist[3]
    madebinaries.append(templist)
    print(templist)
print('Made Binaries')
print(madebinaries)
    
for i in madebinaries:
    for j in i:
        print(chr(j))
        final += str(chr(j))

print(final)
#input()