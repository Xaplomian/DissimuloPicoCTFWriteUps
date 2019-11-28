# vault-door-5
In the last challenge, you mastered octal (base 8), decimal (base 10), and hexadecimal (base 16) numbers, but this vault door uses a different change of base as well as URL encoding! The source code for this vault is here: VaultDoor5.java

Worth 300 points.

## Hints
You may find an encoder/decoder tool helpful, such as https://encoding.tools/
Read the wikipedia articles on URL encoding and base 64 encoding to understand how they work and what the results look like.

## Solution
### Relevant Code
```java
public boolean checkPassword(String password) {
    String urlEncoded = urlEncode(password.getBytes());
    String base64Encoded = base64Encode(urlEncoded.getBytes());
    String expected = "JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVm"
                    + "JTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2"
                    + "JTM0JTVmJTY0JTYyJTM2JTM5JTM0JTM2JTYyJTYx";
    return base64Encoded.equals(expected);
```

To solve this all the base 64 characters need to be put together without the code around in the string `"JTYzJTMwJTZlJTc2JTMzJTcyJTc0JTMxJTZlJTY3JTVmJTY2JTcyJTMwJTZkJTVmJTYyJTYxJTM1JTY1JTVmJTM2JTM0JTVmJTY0JTYyJTM2JTM5JTM0JTM2JTYyJTYx"`. To decode this this string can be put into a [decode website tool](https://www.base64decode.org/).  

This gives the string `"%63%30%6e%76%33%72%74%31%6e%67%5f%66%72%30%6d%5f%62%61%35%65%5f%36%34%5f%64%62%36%39%34%36%62%61"`.  

Paste that into a URL bar in a web browser, which gives the string `"c0nv3rt1ng_fr0m_ba5e_64_db6946ba"`.  

## Flag
Done by: James  
Completed: *During challenge*  
Flag: `picoCTF{c0nv3rt1ng_fr0m_ba5e_64_db6946ba}`  
