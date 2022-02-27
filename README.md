<h1 align="center">
	<img src="https://cdn.discordapp.com/attachments/946797907846258799/946798556629585950/unknown.png" width="150px"><br>
    oCrypt0r - A minimalistic, simple AES encryption library written in python3.
</h1>
<p align="center">
    oCrypt0r allows you to encrypt and decrypt strings of text via AES. Your encrypted data/strings can only be decrypted using your own custom key and salt you set before encrypting said data. You can use this for a variety of things from creating passwords, to encrypting HWIDs and much more!. Making AES encryption a little bit easier!
</p>

<h1></h1>

<br />
<br />

# Updates
What has been updated as of | 2/27/22:

> - Added File encryption & Decryption!
> - Fixed some typos in the readmes's code examples.
> - Removed loading spinner animation when encrypting. (To make it faster and more practical in an automation sense.)
> - Updated my example code all the way at the bottom of this readme.

<br />
<br />

# Installation

```bash
[Directly from here/this repo.]
- pip install git+https://github.com/therealOri/oCrypt0r

or

[From Pypi.]
- pip install oCrypt0r
```
__ __

<br />
<br />

# Code Examples
> Strings/Messages.
```python
from oCrypt0r import oCrypt

#Encrypting Strings
string = input("Enter string: ")
salt = input("Enter salt: ")
encr = oCrypt().string_encrypt(string, salt)
print(encr)


#Decrypting Strings
string2 = input("Enter string: ")
salt2 = input("Enter salt: ")
ecr = oCrypt().string_decrypt(string2, salt2) #Will return "None" if any errors happen.
print(decr)
```

<br />
<br />

> Files

```python
from oCrypt0r import oCrypt


#Encrypting Files
file_path = '/home/ori/Desktop/uwu.txt' #Must be a path to a file you want to encrypt.
salt = input("Enter salt: ")
oCrypt().file_encrypt(file_path, salt)


#Decrypting Files
file_path2 = '/home/ori/Desktop/uwu.txt.oCrypted' # .oCrypted is what is used to let you know that the file is encrypted.
salt2 = input("Enter salt: ")
decr = oCrypt().file_decrypt(file_path2, salt2) #Will return "False" if any errors happen.
```
__ __

My own sample file for this project: [crypt_sample.py](https://haste.powercord.dev/afakewabam.py)
