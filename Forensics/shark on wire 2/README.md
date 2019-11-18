Building on the skills from `shark on wire 1`, you arrive at the program Wireshark

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

the flag is `picoCTF{p1LLf3r3d_data_v1a_st3g0}`
