numbers = [1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734293602, 1701067056, 892756537]
binaries = []
final = ''

for i in numbers:
    num = str(bin(i))[2::]
    binout = int(31 - int(len(num))) * '0' + num
    binaries.append(binout)
print('Binaries')
print(binaries)

madebinaries = []
for i in binaries:
    templist = [int((i[0:7]),2), int((i[8:15]),2), int((i[16:23]),2), int((i[24:31]),2)]
    madebinaries.append(templist)
    print(templist)
print('Made Binaries')
print(madebinaries)
    
for i in madebinaries:
    for j in i:
        print(chr(j))
        final += str(chr(j))

print(final)
input()