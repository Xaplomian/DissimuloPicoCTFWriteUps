# like1000
This .tar file got tarred alot. Also available at /problems/like1000_0_369bbdba2af17750ddf10cc415672f1c. Spelling mistake reproduced.

Worth 250 points.

## Hint
Try and script this, it'll save you alot of time. Spelling mistake reproduced.

## Solution
This is best done with an auto-clicker. Auto hotkey was used to make this. The click position is based off 7-zip being maximised on a 1080p screen.

To make the script, get the position that you need to click with the window spy that comes with Auto hotkey. 
Add an initial wait of 2000 milliseconds to get 7zip open, then put in a loop for 999 repetitions where it clicks twice and has a short delay of 100 milliseconds.

Example Script:
```
Sleep, 2000 ; allows opening program before clicking
Loop 999 {
click, x, y ; change x and y to correct values for your screen
click, x, y
Sleep, 100 ; wait to avoid clicking before new folder loaded
}
```

## Details
Done by: James
Completed: *During challenge*
Flag: `picoCTF{l0t5_0f_TAR5}`