# vault-door-1

This vault uses some complicated arrays! I hope you can make sense of it, special agent. The source code for this vault is here: VaultDoor1.java

Worth 100 points.

## Hint

Look up the charAt() method online.

## Solution
### Relavent Code
```java
public boolean checkPassword(String password) {
    return password.length() == 32 &&
    password.charAt(0)  == 'd' &&
    password.charAt(29) == '8' &&
    password.charAt(4)  == 'r' &&
    password.charAt(2)  == '5' &&
    password.charAt(23) == 'r' &&
    password.charAt(3)  == 'c' &&
    password.charAt(17) == '4' &&
    password.charAt(1)  == '3' &&
    password.charAt(7)  == 'b' &&
    password.charAt(10) == '_' &&
    password.charAt(5)  == '4' &&
    password.charAt(9)  == '3' &&
    password.charAt(11) == 't' &&
    password.charAt(15) == 'c' &&
    password.charAt(8)  == 'l' &&
    password.charAt(12) == 'H' &&
    password.charAt(20) == 'c' &&
    password.charAt(14) == '_' &&
    password.charAt(6)  == 'm' &&
    password.charAt(24) == '5' &&
    password.charAt(18) == 'r' &&
    password.charAt(13) == '3' &&
    password.charAt(19) == '4' &&
    password.charAt(21) == 'T' &&
    password.charAt(16) == 'H' &&
    password.charAt(27) == '3' &&
    password.charAt(30) == '4' &&
    password.charAt(25) == '_' &&
    password.charAt(22) == '3' &&
    password.charAt(28) == 'f' &&
    password.charAt(26) == '0' &&
    password.charAt(31) == '1';
}
```

In the check password function, get all the characters in order based off the index in the string. Use the index values at password.charAt(i). The characters at each index are: `[0 = d, 29 = 8, 4 = r, 2 = 5, 23 = r, 3 = c, 17 = 4, 1 = 3, 7 = b, 10 = _, 5 = 4, 9 = 3, 11 = t, 15 = c, 8 = l, 12 = H, 20 = c, 14 = _, 6 = m, 24 = 5, 18 = r, 13 = 3, 19 = 4 , 21 = T, 16 = H, 27 = 3, 30 = 4, 25 = _, 22 = 3, 28 = f, 26 = 0, 31 = 1]`
When rearranged they form the string: d35cr4mbl3_tH3_cH4r4cT3r5_03f841
Then put this into the correct flag form.

## Details
Done by: James  
Completed: *During challenge*  
Flag: `picoCTF{d35cr4mbl3_tH3_cH4r4cT3r5_03f841}`
