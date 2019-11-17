# vault-door-8
Apparently Dr. Evil's minions knew that our agency was making copies of their source code, because they intentionally sabotaged this source code in order to make it harder for our agents to analyze and crack into! The result is a quite mess, but I trust that my best special agent will find a way to solve it. The source code for this vault is here: VaultDoor8.java

Worth 450 points.

# Hints
Clean up the source code so that you can read it and understand what is going on.
Draw a diagram to illustrate which bits are being switched in the scramble() method, then figure out a sequence of bit switches to undo it. You should be able to reuse the switchBits() method as is.

# Solution
##Relavent Code
```java
//commented out code removed as it is unnecessary
for (int b=0; b<a.length; b++) {
	char c = a[b];
	c = switchBits(c,1,2);
	c = switchBits(c,0,3);
	c = switchBits(c,5,6);
	c = switchBits(c,4,7);
	c = switchBits(c,0,1);
	c = switchBits(c,3,4);
	c = switchBits(c,2,5);
	c = switchBits(c,6,7);
	a[b] = c;
}
		
public char switchBits(char c, int p1, int p2) {
	char mask1 = (char)(1 << p1);
	char mask2 = (char)(1 << p2);
	char bit1 = (char)(c & mask1);
	char bit2 = (char)(c & mask2);
	char rest = (char)(c & ~(mask1 | mask2));
	char shift = (char)(p2 - p1);
	char result = (char)((bit1<<shift) | (bit2>>shift) | rest);
	return result;
}

char[] expected = {0xF4, 0xC0, 0x97, 0xF0, 0x77, 0x97, 0xC0, 0xE4, 0xF0, 0x77, 0xA4, 0xD0, 0xC5, 0x77, 0xF4, 0x86, 0xD0, 0xA5, 0x45, 0x96, 0x27, 0xB5, 0x77, 0x94, 0x85, 0xC0, 0xA5, 0xC0, 0xB4, 0xC2, 0xF0, 0xF0};
```

It is best to write a script to do this, doing this by hand would take too long.

1. Convert Code into readable format. Compare original code to formatted code.
2. Put in the given hex codes into the script to process..
3. Create a bit switch function in your script, for python simply remove the type definitions from the switchBits function in the java.
4. Call the switch bits with the bits given. Make sure to call it in reverse order of calls given in the java. 



# Flag
picoCTF{s0m3_m0r3_b1t_sh1fTiNg_ad0f0c833}