# vault-door-3
This vault uses for-loops and byte arrays. The source code for this vault is here: VaultDoor3.java

Worth 200 points.

## Hint
Make a table that contains each value of the loop variables and the corresponding buffer index that it writes to.

## Solution
### Relevant Code
```java
        char[] buffer = new char[32];
        int i;
        for (i=0; i<8; i++) {
            buffer[i] = password.charAt(i);
        }
        for (; i<16; i++) {
            buffer[i] = password.charAt(23-i);
        }
        for (; i<32; i+=2) {
            buffer[i] = password.charAt(46-i);
        }
        for (i=31; i>=17; i-=2) {
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm1dg347_u_4_mfr54b");
```
To solve go through each for loop and determine where each character's position in the flag is. After each Loop there will be an indication of the flag at that point where unknown characters will be indicated by '0'. A python script was used to do this, it is attached.

Loop 1:
This loop deals with the first 8 characters "jU5t_a_s" These characters are at the beginning of the flag as there is nothing to change the position of the 		character. The flag so far is "jU5t_a_s000000000000000000000000".

Loop 2:
This loop deals with the substring "na_3lpm1". From the code we know that each character's index is equal to 23-[the original index]. We can revers this operation by subtracting the current index from 23 to get the original. We have indices 8-15. This string will appear in revers order within the flag, so we have the substring "1mp13_an". The index of "1" is 15, subtracted from 23 is 8, so it starts and index 8 in the flag, thus directly following the previous string. The flag so far is "jU5t_a_s1mp13_an0000000000000000".

Loop 3:
This loop is more complicated than the other loops because the index is increased by two each loop. It contains the original indices: [16,18,20,22,24,26,28,30]
46-30=16. Like in the last loop we must reverse the order of the digits to get: [30,28,26,24,22,20,18,16]. The characters in the string need to be swapped, based off the two sets of values given. The flag so far is "jU5t_a_s1mp13_an40r0m040u07030d0"

Loop 4:
In this loop we go backwards from 31 to 17. This one is simple and does not move the digits around. So we just put in the characters at the same location to get the orignal string. This makes the flag be: "jU5t_a_s1mp13_an4gr4m_4_u_7f35db"

### Details
Done by: James
Completed: *During challenge*
picoCTF{jU5t_a_s1mp13_an4gr4m_4_u_7f35db}