# shark on wire 2
We found this [packet capture](https://2019shell1.picoctf.com/static/dcd259894e0efe9d6e91da2af47e6369/capture.pcap). Recover the flag that was pilfered from the network. You can also find the file in /problems/shark-on-wire-2_0_3e92bfbdb2f6d0e25b8d019453fdbf07.

## Hint
None

## Solution
Building on the skills from *shark on wire 1*, you arrive at the program Wireshark  
Looking at the udp stream, you can find some 'partial' flags in udp.stream eq 4 to 10. However, they are red herrings / misleading.

When looking at packages where the source if from `10.0.0.66`, you may notice that one package says start. 
The following packages consist of data in the form 5??? -> 22 Len=5
The 3 question marks correspond to the bytes encoding of the flag.

e.g. 
5112 -> 112 -> p
5105 -> 105 -> i
5099 -> 099 -> c
5111 -> 111 -> o
...


## Details
Done by: Cyril
Completed: After challenge  
Flag: `picoCTF{p1LLf3r3d_data_v1a_st3g0}`