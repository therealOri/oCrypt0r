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
What has been updated as of | 7/17/22:

> - Encryption functions now take 3 args instead of 4.
> - Removed the hashing feature that makes a blake2b hash of a key to be used in the encryption. This basically made things less unique as the hash was just all 0-9 and lowercase a-z characters.

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

It is important to know that all functions will take 3 values. 2 for the making of the encryption key, and 1 for what you want encrypted/decrypted.

The encryption takes 2 values to make a key. The key then gets plugged into the AES encryption as a cipher. All of that will be used to encrypt whatever you want as a value. "strings", "files", or "directories/folders". (inclusing sub-directories)

You can read more about what the arguments do in the documentation.

- [Documentation](https://github.com/therealOri/oCrypt0r/blob/main/DOCUMENTATION.md)
```python
from ocryptor import oCrypt


##---------Strings---------##

#Encrypting Strings
string = 'Hello Wolrd <3'
enc_key = "abcdefgHIJKLMNOP~!@#$%^&*"
enc_salt = 'qrstuvwxyz1234567890'

str_enc = oCrypt().string_encrypt(string, enc_key, enc_salt)
print(str_enc) # Output is b64 encoded. => VpqFynzUPOK3dHYaCFO57IGlYrQRyzt2NvmzMEN2+AA=



#Decrypting Strings
string = 'VpqFynzUPOK3dHYaCFO57IGlYrQRyzt2NvmzMEN2+AA='
enc_key = "abcdefgHIJKLMNOP~!@#$%^&*"
enc_salt = 'qrstuvwxyz1234567890'

str_dcr = oCrypt().string_decrypt(string, enc_key, enc_salt)
print(str_dcr) # Output is "Hello Wolrd <3"

##---------Strings End---------##







##---------Files---------##

#Encrypting Files
file_path = '/home/therealOri/Projects/example.txt'
enc_key = "abcdefgHIJKLMNOP~!@#$%^&*"
enc_salt = 'qrstuvwxyz1234567890'

oCrypt().file_encrypt(file_path, enc_key, enc_salt)



#Decrypting Files
file_path = '/home/therealOri/Projects/example.txt.oCrypted' # .oCrypted is what is used to let you know that the file is encrypted.
enc_key = "abcdefgHIJKLMNOP~!@#$%^&*"
enc_salt = 'qrstuvwxyz1234567890'

oCrypt().file_decrypt(file_path, enc_key, enc_salt)

##---------Files End---------##







##---------Directories---------##

#Encrypting Directory
dir_path = '/home/therealOri/Projects' #Must be a path to the directory you want to encrypt.
enc_key = "abcdefgHIJKLMNOP~!@#$%^&*"
enc_salt = 'qrstuvwxyz1234567890'

oCrypt().dir_encrypt(dir_path, enc_key, enc_salt)



#Decrypting Directory
dir_path = '/home/therealOri/Projects'
enc_key = "abcdefgHIJKLMNOP~!@#$%^&*"
enc_salt = 'qrstuvwxyz1234567890'

oCrypt().dir_decrypt(dir_path, enc_key, enc_salt)

##---------Directories End---------##
```

<br />

__ __

<br />

# Disclaimer
I am not liable or responsible for any data loss or destruction of any kind of data perpetrated by bad actors using my code/package/functions. This also extends to losing your own data while using oCrypt0r. If you lose data and do not have backups then that is solely on you and I am not liable or responible for any loss of data you may have occured.
__ __



<br />

# Support  |  Buy me a coffee <3
Donate to me here:
> - Don't have Cashapp? [Sign Up](https://cash.app/app/TKWGCRT)

![image](https://user-images.githubusercontent.com/45724082/158000721-33c00c3e-68bb-4ee3-a2ae-aefa549cfb33.png)

