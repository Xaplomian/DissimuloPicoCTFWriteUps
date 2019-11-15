#vault-door-1
This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: VaultDoor1.java

Worth 100 points.

#Hint
Look up the charAt() method online.

#Solution
In the check password function, get all the characters in order based off the index in the string. Use the index values at password.charAt(i). The characters at each index are ``` [0 = d, 29 = 8, 4 = r, 2 = 5, 23 = r, 3 = c, 17 = 4, 1 = 3, 7 = b, 10 = _, 5 = 4, 9 = 3, 11 = t, 15 = c, 8 = l, 12 = H, 20 = c, 14 = _, 6 = m, 24 = 5, 18 = r, 13 = 3, 19 = 4 , 21 = T, 16 = H, 27 = 3, 30 = 4, 25 = _, 22 = 3, 28 = f, 26 = 0, 31 = 1] ```
When rearranged they form the string: d35cr4mbl3_tH3_cH4r4cT3r5_03f841
Then put this into the correct flag form

#Flag
picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_03f841}