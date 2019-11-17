basestring = 'jU5t_a_sna_3lpm1dg347_u_4_mfr54b'
output = [1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

for i in range(0,8):
    output[i] = basestring[i]

temp = i

for i in range(temp, 17):
    output[23-i] = basestring[i]


while i<32:
    output[46-i] = basestring[i]
    i+=2

i = 31

while i >= 17:
    output[i] = basestring[i]
    i -= 2
print(output)    
print(''.join(output))
input('')

