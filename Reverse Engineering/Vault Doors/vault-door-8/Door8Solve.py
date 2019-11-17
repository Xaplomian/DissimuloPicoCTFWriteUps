hexcodes = ['F4', 'C0', '97', 'F0', '77', '97', 'C0', 'E4', 'F0', '77', 'A4', 'D0', 'C5', '77', 'F4', '86', 'D0', 'A5', '45', '96', '27', 'B5', '77', '94', '85', 'C0', 'A5', 'C0', 'B4', 'C2', 'F0', 'F0']

def bitswitch(num, p1,p2):
    mask1 = 1 << p1
    mask2 = 1 << p2
    bit1 = num & mask1
    bit2 = num & mask2
    rest = num & ~(mask1 | mask2)
    shift = (p2-p1)
    result = ((bit1<<shift) | (bit2>>shift) | rest)
    return result
output = ''


for i in hexcodes:
    dec = int(i, 16)
    temp = dec
    dec = bitswitch(dec,6,7)
    dec = bitswitch(dec,2,5)
    dec = bitswitch(dec,3,4)
    dec = bitswitch(dec,0,1)
    dec = bitswitch(dec,4,7)
    dec = bitswitch(dec,5,6)
    dec = bitswitch(dec,0,3)
    dec = bitswitch(dec,1,2)
    output += chr(dec)   
    print(str(temp) + ', ' +  str(dec))
print(output)
input()