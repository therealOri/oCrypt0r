<h1 align="center">
	<img src="https://cdn.discordapp.com/attachments/946797907846258799/946798556629585950/unknown.png" width="150px"><br>
    oCrypt0r - A minimalistic, simple AES encryption library written in python3.
</h1>
<p align="center">
    oCrypt0r allows you to encrypt and decrypt strings of text via AES. Your encrypted data/strings can only be decrypted using your own custom key and salt you set before encrypting said data. You can use this for a variety of things from securing passwords to securing communication to encrypting HWIDs and directories/folders. Making AES encryption a little bit easier!
</p>

<h1></h1>

<br />
<br />

# Updates
What has been updated as of | 2/28/22:

> - New way of hashing and salting said hash.
> - Documentation file added to this repo.
> - Updated code file and examples.

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

It is important to know that all functions will take 4 values. 2 for the making of the hashed value and 2 for the making of the encryption key.
Blake2b salted hashing requires 1 value to be hashed and 1 value to be used to salt the hash. This then gets plugged into the AES encryption as a key and then we salt that aswell. All of that will be used to encrypt whatever you want as a value. "strings", "files", or "directories/folders".

- [Documentation](https://github.com/therealOri/oCrypt0r/blob/main/DOCUMENTATION.md)
```python
from ocryptor import oCrypt


##---------Strings---------##

#Encrypting Strings
key = input("Enter word for hashing: ")
key_salt = input("Enter salt for hashing: ")
string = input("Enter string: ")
string_salt = input("Enter salt for encryption: ")
str_enc = oCrypt().string_encrypt(key, key_salt, string, string_salt)
print(string_enc)


#Decrypting Strings
key2 = input("Enter the word you used for hashing: ")
key_salt2 = input("Enter the salt you used for hashing: ")
string2 = input("Enter your string to decrypt: ")
salt2 = input("Enter the salt you used for encryption: ")
str_dcr = oCrypt().string_decrypt(key2, key_salt2, string2, string_salt2) # Will return "False" if errors happen. "True" if successful.
print(str_dcr)

##---------Strings End---------##





##---------Files---------##

#Encrypting Files
key = input("Enter word for hashing: ")
key_salt = input("Enter salt for hashing: ")
file_path = '/home/ori/Desktop/uwu.txt' #Must be a path to a file you want to encrypt.
file_salt = input("Enter salt for encryption: ")
oCrypt().file_encrypt(key, key_salt, file_path, file_salt) # Will return "False" if errors happen. "True" if successful.


#Decrypting Files
key2 = input("Enter the word you used for hashing: ")
key_salt2 = input("Enter the salt you used for hashing: ")
file_path2 = '/home/ori/Desktop/uwu.txt.oCrypted' # .oCrypted is what is used to let you know that the file is encrypted.
file_salt2 = input("Enter the salt you used for encryption: ")
oCrypt().file_decrypt(key, key_salt, file_path2, file_salt2)

##---------Files End---------##





##---------Directories---------##

#Encrypting Directory
key = input("Enter word for hashing: ")
key_salt = input("Enter salt for hashing: ")
dir_path = '/home/ori/Desktop/testing' #Must be a path to the directory you want to encrypt.
dir_salt = input("Enter salt for encryption: ")
oCrypt().dir_encrypt(key, key_salt, dir_path, dir_salt) # Will return "False" if errors happen. "True" if successful.


#Decrypting Directory
key2 = input("Enter the word you used for hashing: ")
key_salt2 = input("Enter the salt you used for hashing: ")
dir_path2 = '/home/ori/Desktop/testing' # .oCrypted is what is used to let you know that the file is encrypted.
dir_salt2 = input("Enter the salt you used for encryption: ")
oCrypt().dir_decrypt(key2, sdir_salt2, dir_path2, sdir_salt2)

##---------Directories End---------##
```

<br />

__ __

My own sample file for this project: [crypt_sample.py](https://haste.powercord.dev/atehenepos.py) 
