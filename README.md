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
What has been updated as of | 2/25/22:

> Created this repo!

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

# Code Example

```python
from ocryptor import oCrypt

#Encrypting
string = input("Enter string: ")
salt = input("Enter salt: ")
encr = oCrypt.Encrypt(string, salt)
print(encr)


#Decrypting
string2 = input("Enter string: ")
salt2 = input("Enter salt: ")
decr = Crypt0r().Decrypt(string2, salt2) #Will return "None" if any errors happen.
print(decr)
```
__ __

My own sample file for this project: [oCrypt0r_sample.py](https://haste.powercord.dev/xeluzohute.py)
