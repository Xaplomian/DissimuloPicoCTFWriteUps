# vault-door-6
This vault uses an XOR encryption scheme. The source code for this vault is here: VaultDoor6.java

Worth 600 points.

# Hint
If X ^ Y = Z, then Z ^ Y = X. Write a program that decrypts the flag based on this fact.

# Solution
## Relavent Code
```java
byte[] passBytes = password.getBytes();
byte[] myBytes = {
    0x3b, 0x65, 0x21, 0xa , 0x38, 0x0 , 0x36, 0x1d,
    0xa , 0x3d, 0x61, 0x27, 0x11, 0x66, 0x27, 0xa ,
    0x21, 0x1d, 0x61, 0x3b, 0xa , 0x2d, 0x65, 0x27,
    0xa , 0x34, 0x30, 0x31, 0x30, 0x36, 0x30, 0x31,
};
for (int i=0; i<32; i++) {
    if (((passBytes[i] ^ 0x55) - myBytes[i]) != 0) {
        return false;
    }
}
```
This was done primarily with python scripts, a python script is attached.

1. Convert the hex values to binary. A length of seven binary digits is needed, so that each value has the same number of digits to compare against the key. Eight is not needed, because if there was eight each value would have 0 first which is unnecessary processing. 
	1. Convert the key. The key is the hex character in `if (((passBytes[i] ^ 0x55)`. It is best to do this by hand from an ASCII table.
	2. Convert the myBytes, into binary. It is best to get a computer to do this. 
2. Apply the XOR operation. The truth table is bellow. Do not do this by hand, it will take far too long, it is 224 operations to do,
	Key bit | Value Bit | Result Bit
	--------| ---------
	0 | 0 | 0
	0 | 1 | 1
	1 | 0 | 1
	1 | 1 | 0
3. Convert the resulting binaries into their ASCII digits.
4. Get the flag.


# Flag
picoCTF{n0t_mUcH_h4rD3r_tH4n_x0r_aedeced}