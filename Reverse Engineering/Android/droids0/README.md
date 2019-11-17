# droids0
Where do droid logs go. Check out this [file](thanks for putt the file james). You can also find the file in /problems/droids0_0_205f7b4a3b23490adffddfcfc45a2ca3.

# Hint
Try using an emulator or device
https://developer.android.com/studio

# Details
Completed: **During challenge**  
Flag: `picoCTF{a.moose.once.bit.my.sister}`

# Solution
1. Download Android Studio
1. Create a new blank application
1. Setup an Android Virtual Device (AVD)
1. Install the zero.apk onto the AVD through the picoctf website (very janky)
1. Open logcat in Android Studio
1. Run the app on the AVD
1. Enter something into the field and click the button
1. Search the output for "picoctf" on the logcat screen
1. Get the flag
