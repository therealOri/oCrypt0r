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
What has been updated as of | 3/02/22:

> - dir_encrypt() & dir_decrypt() will now ignore files with no data.
> - dir_decrypt() will ignore files without the extension `.oCrypted`.
> - file_encrypt() & file_decrypt() will both now throw/raise proper errors if the file they are encrypting/decrypting has/contains no data.

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

It is important to know that all functions will take 4 values. 2 for the making of the hashed value, 1 for the making of the encryption key, and 1 for what you want encrypted/decrypted.

Blake2b salted hashing requires 1 value to be hashed and 1 value to be used to salt the hash. This then gets plugged into the AES encryption as a key and then we salt that aswell. All of that will be used to encrypt whatever you want as a value. "strings", "files", or "directories/folders".

You can read more about what the arguments do in the linked documentation.

- [Documentation](https://github.com/therealOri/oCrypt0r/blob/main/DOCUMENTATION.md)
```python
from ocryptor import oCrypt


##---------Strings---------##

#Encrypting Strings
key = 'therealOri'
key_salt = 'abcdefghijklmnop' #MUST be 16 characters or less.
string = 'Hello Wolrd <3'
enc_salt = 'qrstuvwxyz1234567890'

str_enc = oCrypt().string_encrypt(key, key_salt, string, enc_salt)
print(str_enc) # Output is b64 encoded.



#Decrypting Strings
key = 'therealOri'
key_salt = 'abcdefghijklmnop'
string = 'Hello Wolrd <3'
enc_salt = 'qrstuvwxyz123456'

str_dcr = oCrypt().string_decrypt(key, key_salt, string, enc_salt)
print(str_dcr) # Output is "Hello Wolrd <3"

##---------Strings End---------##







##---------Files---------##

#Encrypting Files
key = 'therealOri'
key_salt = 'abcdefghijklmnop'
file_path = '/home/therealOri/Projects/example.txt'
enc_salt = 'qrstuvwxyz123456'

oCrypt().file_encrypt(key, key_salt, file_path, enc_salt)



#Decrypting Files
key = 'therealOri'
key_salt = 'abcdefghijklmnop'
file_path = '/home/therealOri/Projects/example.txt.oCrypted' # .oCrypted is what is used to let you know that the file is encrypted.
enc_salt = 'qrstuvwxyz123456'

oCrypt().file_decrypt(key, key_salt, file_path, enc_salt)

##---------Files End---------##







##---------Directories---------##

#Encrypting Directory
key = 'therealOri'
key_salt = 'abcdefghijklmnop'
dir_path = '/home/therealOri/Projects' #Must be a path to the directory you want to encrypt.
enc_salt = 'qrstuvwxyz123456'

oCrypt().dir_encrypt(key, key_salt, dir_path, enc_salt)



#Decrypting Directory
key = 'therealOri'
key_salt = 'abcdefghijklmnop'
dir_path = '/home/therealOri/Projects'
enc_salt = 'qrstuvwxyz123456'

oCrypt().dir_decrypt(key2, sdir_salt2, dir_path2, sdir_salt2)

##---------Directories End---------##
```

<br />

__ __

<br />

# Support  |  Buy me a coffee <3
Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)

