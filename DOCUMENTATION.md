# oCrypt0r Functions Documentation
This is the documentation for the code examples in the README.md file.
__ __

<br />
<br />

# String Encryption
> oCrypt() is the class name.
```python
string_encrypt(key, key_salt, string, enc_salt)
```
`string_encrypt()` is the function used to encrypt a string. It accepts strings as arguments.
> It takes 4 arguments, 2 for the blake2b hash&salt, and 2 for the encryption key and what you want to encrypt. "string" Is what you want to have encrypted.

```python
string_decrypt(key, key_salt, string, enc_salt)
```
`string_decrypt()` is the function used to decrypt a string. It takes the same arguments as above and uses them to decrypt "string".
__ __

**Arguments:**
- `key` = Word you want hashed.
- `key_salt` = A salt for that hash.
- `string` = What you want to be encrypted.
- `enc_salt` = A salt that will be used for the encryption.


__ __

<br />
<br />

# File Encryption
> oCrypt() is the class name.
```python
file_encrypt(key, key_salt, file_path, enc_salt)
```
`file_encrypt()` is the function used to encrypt files. 
> It takes 4 arguments, 2 for the blake2b hash&salt, and 2 for the encryption key and what you want to encrypt. "file_path" Is what you want to have encrypted.
> "file_path" MUST be the absolute path of the file. Example: "/home/therealOri/Desktop/Project/example.txt"

```python
file_decrypt(key, key_salt, file_path, enc_salt)
```
`file_decrypt()` is the function used to decrypt a file. It takes the same arguments as above and uses them to decrypt "file_path". AKA your file.
__ __

**Arguments:**
- `file_path` = The path to the file you want encrypted. Example: `/home/therealOri/Projects/example.txt`
__ __

<br />
<br />

# Directory Encryption | Folder Encryption
> oCrypt() is the class name.
```python
dir_encrypt(key, key_salt, dir_path, enc_salt)
```
`dir_encrypt()` is the function used to encrypt directories/folders. 
> It takes 4 arguments, 2 for the blake2b hash&salt, and 2 for the encryption key and what you want to encrypt. "dir_path" Is what you want to have encrypted.
> "dir_path" MUST be the absolute path to the directory/folder. Example: "/home/therealOri/Desktop/Projects"
> If there are sub directories (folders in folders), it will encrypt the files in there aswell.

```python
dir_decrypt(key, key_salt, dir_path, dir_salt)
```
`dir_decrypt()` is the function used to decrypt a directory. It takes the same arguments as above and uses them to decrypt "dir_path". AKA your directory/folder.
__ __

**Arguments:**
- `dir_path` = The path to the folder/directory you want encrypted. Example: `/home/therealOri/Projects/Example`

__ __

<br />
<br />

# About | FAQs
> - [Q1] Why so many arguments?
> 
> - [A1] To achieve high security, I don't want to have the actual strings/variables just there in the open, set as variables in the code for anyone to decode and read, etc. So instead of me deciding what strings/variables should be used in the salted blake2b hash. I want YOU do decide that and to make it even more unique, with your own information.

<br />
<br />

> - [Q2] What does blake2b, hash, and salted hash mean?
>
> - [A2] BLAKE2 is a cryptographic hash function.  |  Hashes are the output of a hashing algorithm like, for example blake2b. These algorithms essentially aim to produce a unique, fixed-length string(the hash value), or (message digest) – for any given piece of data or “message”. As every file on a computer is, ultimately, just data that can be represented in binary form, a hashing algorithm can take that data and run a complex calculation on it and output a fixed-length string as the result of the calculation. The result is the file’s hash value or message digest.  |  SALTING is the process of adding a unique value to the end of a password before hashing takes place. Salting the hash is crucial because it ensures that the encryption process results in a different hash value, even when two passwords are the same.

<br />
<br />

> - [Q3] What is the purpose of this package/library.
> 
> - [A4] To allow you to encrypt and decrypt anything you want pretty fast and easily. To use it in your code when you need to encrypt something or decrypt something. To encrypt everything in a specified folder to make sure people can't just snoop around easily. To bring you AES encryption without the hastle of setting everything up yourself. All you'll need to do is provide the information it asks for and it'll do all the work for you.
__ __

- You can read more about what "Hashing" is here: https://www.sentinelone.com/cybersecurity-101/hashing/ 
- You can read more about "Blake2b" here: https://www.blake2.net.
- And you can read more about "Salting" here: https://www.omnicybersecurity.com/what-does-salting-the-hash-mean-is-it-effective/
__ __
