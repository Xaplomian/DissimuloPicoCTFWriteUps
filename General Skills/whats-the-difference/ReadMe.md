# whats-the-difference
Can you spot the difference? kitters cattos. They are also available at /problems/whats-the-difference_0_00862749a2aeb45993f36cc9cf98a47a on the shell server

## Hint
How do you find the difference between two files?
Dumping the data from a hex editor may make it easier to compare.

## Solution
The Hex editor HxD was used to solve this, and the solution will refer specifically to this program.

1. Open each image file in HxD.
2. Go to Analysis>Data Comparison>Compare... Ctrl+K
	a. In the Dialogue Box the two data sources should be the two images we have. If this it not the case add them in.
	b. Click OK
3. Record the data highlighted in cattos.jpg, then go to the next character (using F6) and record that. Repeat until the end of the document has been reached.


## Details
Done by: James
Completed: *During challenge*
Flag: `picoCTF{th3yr3_a5_d1ff3r3nt_4s_bu773r_4nd_j3lly_aslkjfdsalkfslkflkjdsfdszmz10548}`