This was a medium-difficulty reverse-engineering challenge for the member-made SUCSS competition
# Interface
The challenge was redirecting us to a static website where it was requesting a password to give us the flag
[interface.png]
Since there were no network packets pointing to a backend server or any calls to an api endpoint, the password checking should have been done locally.
By having a look at the source files I found a very strange index.js file that was clearly an obfuscated js file
[index.js.png]
So I tried to run it line by line on the console to statically deobfuscate it.
After doing a little static analysis and replacing the bits that were not recongnizable by the node compiler, I build the test.js file which I then run locally and I printed the last - very long line which was the obfuscated function to see exactly what operations it was performing.
[deobfuscated.png]
