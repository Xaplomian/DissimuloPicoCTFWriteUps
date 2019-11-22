# vault-door-4
This vault uses ASCII encoding for the password. The source code for this vault is here: VaultDoor4.java

Worth 250 points

## Hints
Use a search engine to find an "ASCII table".
You will also need to know the difference between octal, decimal, and hexademical numbers. //The spelling mistake is present on the site.

## Solution
### Relevant Code
```java
byte[] myBytes = {
    106 , 85  , 53  , 116 , 95  , 52  , 95  , 98  ,
    0x55, 0x6e, 0x43, 0x68, 0x5f, 0x30, 0x66, 0x5f,
    0142, 0131, 0164, 063 , 0163, 0137, 063 , 0141,
    '7' , '2' , '4' , 'c' , '8' , 'f' , '9' , '2' ,
    };
```

Each of these lines is in a different base. Line 1 is in decimal, line 2 is in hexadecimal, line 3 is in octal, and line 4 is in ASCII. Each term needs to be converted to ASCII.
Line 1: jU5t_4_b
Line 2: UnCh_0f_
Line 3: byt3s_ca
Line 4: 724c8f92
Putting this all together: jU5t_4_bUnCh_0f_byt3s_ca724c8f92

### Flag
Done by: James
Completed: *During challenge*
picoCTF{jU5t_4_bUnCh_0f_byt3s_ca724c8f92}