# Shark on Wire 1

We found this [packet capture](https://2019shell1.picoctf.com/static/ae9ca8cff43ed638ed5d137f9ece7455/capture.pcap). Recover the flag. You can also find the file in /problems/shark-on-wire-1_0_13d709ec13952807e477ba1b5404e620.

# Hint
Try using a tool like Wireshark  
What are streams?

# Details
Completed: **During challenge**  
Flag: `picoCTF{StaT31355_636f6e6e}`

# Solution

The name 'shark' on a 'wire' hints at a program called "Wireshark".  
This can also be also found by searching for "how to open .pcap extension"  
Once opening capture.pcap with wireshark, follow udp.stream eq 6. This will give the flag. 

