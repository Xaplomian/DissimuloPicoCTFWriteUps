#This program was slightly modified after the competition ended. Two different programs were joined and code was added at the end to convert to ASCII. It was originally was done by binary decode. The code to homogenise the length of the binary was added afterwards as well, it was ordinally done with a separate script, due to not being considered when first doing it. Some variables were also renamed for clarity.
list = [0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d, 0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa, 0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27, 0xa , 0x34, 0x30, 0x31, 0x30, 0x36, 0x30, 0x31] #Hex Characters from challenge
binaries = []

print('Printing Intital Binaries')
#Converts hex to binary and homgenises length
for i in list:
    bin0 = str(bin(i))[2::]
    bin1 = (7 - len(bin0)) * '0' + bin0
    print(bin1)
    binaries.append(bin1)
print(binaries)
print('\n')
#XOR Shift in Binaries
converted = []
print('Printing converted Binaries')
#Key: 1010101
for string in binaries:
    output = '0'
    if string[0] == '0':
        output += '1'
    else:
        output += '0'
        
    if string[1] == '0':
        output += '0'
    else:
        output += '1'    

    if string[2] == '0':
        output += '1'
    else:
        output += '0'
        
    if string[3] == '0':
        output += '0'
    else:
        output += '1'   

    if string[4] == '0':
        output += '1'
    else:
        output += '0'
        
    if string[5] == '0':
        output += '0'
    else:
        output += '1'  

    if string[6] == '0':
        output += '1'
    else:
        output += '0'

    print(output)
    converted.append(output)
    output = ''
print(converted)
print('\n')

print('Print ASCII')
#Convert Binary to ASCII
Ascii = ''
for i in converted:
    print(chr(int(i,2)))
    Ascii += chr(int(i,2))
print(Ascii)

input()