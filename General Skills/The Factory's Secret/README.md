# The Factory's Secret
There appear to be some mysterious glyphs hidden inside this [abandoned factory](https://2019game.picoctf.com/game)... I wonder what would happen if you collected them all? (1 point)

# Hint
Submit your answer in our competition's flag format. For example, if you answer was 'hello', you would submit 'picoCTF{hello}' as the flag.

# Solution
Go to the game version of the picoCTF challenge (located in the game tab of the website). In the entrance to the general skills room, there is one glyph. Also in that room are two blocks - one short, one long. They do a series of flashes, the short one doing a short flash accompanied with a short beep, and the long block making a long flash and a longer beep. This seems to indicate a morse code cipher. Decoding it after the long gap gives "PILLAR2413" (note: the sequence may be different for different players). When you go into the reversing room, you should turn on the levers in that order (pillar 2, then pillar 4, then pillar 1, then pillar 3), and you will get your glyph. In the web exploitation room, there will be a secret entrance along the bottom wall on the platform to the right of the main entrance, leading you to the glyph. In the binary exploitation room, if you go through the doors in an alternating pattern, eventually a yellow door will reveal, leading you to the next glyph. For cryptography, search every grave, until one of them gets mounted up, allowing you to collect your glyph. Finally, in the forensics room, there will be a pond. There will be a moving ripple in the pond, near the edge of it, and if you press while you're next to the ripple, you'll get the glyph.

Once you get all 6 glyphs, they will form a QR code, with the output `password: xmfv53uqkf621gakvh502gxfu1g78glds`. The string of text can then be put in as the password for the computer in the beginning room of the gamepage. Once inputted, a dialogue will initiate, where one of `the_artist` will suggest `zerozerozerozero` instead of `0000`. 

Submit the flag as picoCTF{zerozerozerozero}
