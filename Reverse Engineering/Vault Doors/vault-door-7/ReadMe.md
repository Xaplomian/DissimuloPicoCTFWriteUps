# vault-door-7
This vault uses bit shifts to convert a password string into an array of integers. Hurry, agent, we are running out of time to stop Dr. Evil's nefarious plans! The source code for this vault is here: VaultDoor7.java

Worth 400 points.

# Hints
Use a decimal/hexademical converter such as this one: https://www.mathsisfun.com/binary-decimal-hexadecimal-converter.html
You will also need to consult an ASCII table such as this one: https://www.asciitable.com/

# Solution
## Relevant Code
```java
public int[] passwordToIntArray(String hex) {
int[] x = new int[8];
byte[] hexBytes = hex.getBytes();
for (int i=0; i<8; i++) {
    x[i] = hexBytes[i*4]   << 24
    | hexBytes[i*4+1] << 16
    | hexBytes[i*4+2] << 8
    | hexBytes[i*4+3];
    }
    return x;
}

    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        int[] x = passwordToIntArray(password);
        return x[0] == 1096770097
            && x[1] == 1952395366
            && x[2] == 1600270708
            && x[3] == 1601398833
            && x[4] == 1716808014
            && x[5] == 1734293602
            && x[6] == 1701067056
        
```

1. Convert each decimal number into binary.
2. Split the long binary number into four binary numbers of length eight.
3. Convert each binary number to its ASCII character.
4. You have your flag. 

Also refer to attached python script.

# Flag
picoCTF{A_b1t_0f_b1t_sh1fTiNg_8bed9056b9}