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
> - A new way to encrypt a specified directory. It will encrypt all of the files in that directory and sub-directories. So if there are folders in folders..it'll do them too.
> - How error handling is done, functions will now return "False" if any errors happen and "True" if successful. Instead of "None"
> - Updated README.md file code examples and how they are presented.

<br />
<br />

# Installation
 > [Directly from here/this repo.]
```bash
[therealOri ~]$ pip install git+https://github.com/therealOri/oCrypt0r
```

or

> [From Pypi.]
```bash
[therealOri ~]$ pip install oCrypt0r
```
__ __

<br />
<br />

# Code Examples
> If you would like to make this look better/more presentable. Please by all means make a pull request xD. I'm not the best with making things look great.
```python
from oCrypt0r import oCrypt


##---------Strings---------##

#Encrypting Strings
string = input("Enter string: ")
salt = input("Enter salt: ")
str_enc = oCrypt().string_encrypt(string, salt)
print(string_enc)


#Decrypting Strings
string2 = input("Enter string: ")
salt2 = input("Enter salt: ")
str_dcr = oCrypt().string_decrypt(string2, salt2) # Will return "False" if errors happen. "True" if successful.
print(str_dcr)

##---------Strings End---------##





##---------Files---------##

#Encrypting Files
file_path = '/home/ori/Desktop/uwu.txt' #Must be a path to a file you want to encrypt.
file_salt = input("Enter salt: ")
oCrypt().file_encrypt(file_path, file_salt) # Will return "False" if errors happen. "True" if successful.


#Decrypting Files
file_path2 = '/home/ori/Desktop/uwu.txt.oCrypted' # .oCrypted is what is used to let you know that the file is encrypted.
file_salt2 = input("Enter salt: ")
oCrypt().file_decrypt(file_path2, file_salt2)

##---------Files End---------##





##---------Directories---------##

#Encrypting Directory
dir_path1 = '/home/ori/Desktop/testing' #Must be a path to the directory you want to encrypt.
dir_salt1 = input("Enter salt: ")
oCrypt().dir_encrypt(dir_path1, dir_salt1) # Will return "False" if errors happen. "True" if successful.


#Decrypting Directory
dir_path2 = '/home/ori/Desktop/testing' # .oCrypted is what is used to let you know that the file is encrypted.
dir_salt2 = input("Enter salt: ")
oCrypt().dir_decrypt(dir_path2, sdir_salt2)

##---------Directories End---------##
```

<br />

__ __

My own sample file for this project: [crypt_sample.py](https://haste.powercord.dev/atehenepos.py)
