# Set 1

This set aims to be the 'getting started' set. The goal of each problem is to figure out the password required by each program. You can look at the source of each program, you can modify the code, but the challenge is that you crack the passwords for the unaltered versions.

## 1-1

This one is just a matter of looking at the code and figuring out how it works.

## 1-2

This code uses the concept of the Caesar Cipher, and expects the password to be the result of applying the [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher). The cipher here is a little different from some applications: the shifting isn't taking place in the English alphabet, but using the underlying computer representation of the characters (see [ASCII codes](http://www.asciitable.com/) or [UTF-8 codes](http://www.utf8-chartable.de/)). The traditional Caesar Cipher just changes letters, but in this case every character is 'shifted', so take that into consideration.

## 1-3

This code is similar to the first set, but has been obfuscated (to make obscure, to make the code hard to read). It was obfuscated using [pyminifier](https://github.com/liftoff/pyminifier), which is pretty cool, though the output may require tweaking to work.

Anywho, the challenge with this scenario is to figure out how the code works, despite being horrible in terms of readability.

## 1-4

This is a very simple hashing example. The password is taken and converted into a hash (typically a constant length number or string), and you need to figure out what passwords create the correct hash value.
