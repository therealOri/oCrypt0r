# oCrypt0r Functions Documentation
This is the documentation for the code examples in the README.md file.
__ __

<br />
<br />

# String Encryption
> oCrypt() is the class name.
```python
string_encrypt(string, enc_key, enc_salt)
```
`string_encrypt()` is the function used to encrypt a string. It accepts strings as arguments.
> It takes 3 arguments, 2 for the encryption and 1 for what you want to encrypt. "string" Is what you want to have encrypted.

<br />
<br />

```python
string_decrypt(string, enc_key, enc_salt)
```
`string_decrypt()` is the function used to decrypt a string. It takes the same 3 arguments as above and uses them to decrypt "string".
__ __

**Arguments:**
- `string` = What you want to be encrypted.
- `enc_key` = The key used to encrypt the string.
- `enc_salt` = A salt that will be used with the key for the encryption.


__ __

<br />
<br />

# File Encryption
> oCrypt() is the class name.
```python
file_encrypt(file_path, enc_key, enc_salt)
```
`file_encrypt()` is the function used to encrypt files. 
> - It takes 3 arguments, 2 for the encryption and 1 for what you want to encrypt. "file_path" Is what you want to have encrypted.
> - "file_path" MUST be the absolute path of the file. Example: "/home/therealOri/Desktop/Project/example.txt"
> - If a file that it is trying to encrypt has no data to encrypt, it will raise/throw an error.

<br />
<br />

```python
file_decrypt(file_path, enc_key, enc_salt)
```
`file_decrypt()` is the function used to decrypt a file. It takes the same arguments as above and uses them to decrypt "file_path". AKA your file. 
> - This function will ignore all files without the ".oCrypted" extension. The file MUST end with that extenstion or else it won't decrypt the file(s).
> - If the file has no data to decrypt, it will throw/raise an error. and say `"File is empty..nothing to decrypt"`.
__ __

**Arguments:**
- `file_path` = The path to the file you want encrypted. 
> Example: `/home/therealOri/Projects/example.txt` for encrypting and `example.txt.oCrypted` for decrypting.
- `enc_key` = The key used to encrypt the string.
- `enc_salt` = A salt that will be used with the key for the encryption.
__ __

<br />
<br />

# Directory Encryption | Folder Encryption
> oCrypt() is the class name.
```python
dir_encrypt(dir_path, enc_key, enc_salt)
```
`dir_encrypt()` is the function used to encrypt directories/folders. 
> - It takes 3 arguments, 2 for the the encryption and 1 for what you want to encrypt. "dir_path" Is what you want to have encrypted. Everything in that directory including sub directories will be encrypted.
> - "dir_path" MUST be the absolute path to the directory/folder. Example: "/home/therealOri/Desktop/Projects"
> - If there are files with no data/empty in the specified directory/subdirectories, it will ignore them and move on to file that DO have data to encrypt.

<br />
<br />

```python
dir_decrypt(dir_path, enc_key, enc_salt)
```
`dir_decrypt()` is the function used to decrypt a directory. It takes the same arguments as above and uses them to decrypt "dir_path". AKA your directory/folder.
> - If a file doesn't have the file extension `.oCrypted` OR if the file has no data to decrypt/is empty, it will ignore the file and move on to the files that DO have data to decrypt. This also applies to subdirectories in the specified directory.
__ __

**Arguments:**
- `dir_path` = The path to the folder/directory you want encrypted. Example: `/home/therealOri/Projects/Example`
- `enc_key` = The key used to encrypt the string.
- `enc_salt` = A salt that will be used with the key for the encryption.

__ __

<br />
<br />

# Clearing Terminal & Windows
```python
clear()
```
`clear()` is the function used to clear your terminal or window.. It takes NO arguments.
> - If you ever need to clear your terminal or window, you can use this instead of making your own way.
__ __

<br />
<br />

# About | FAQs
> - [Q1] What is the purpose of this package/library.
> 
> - [A1] To allow you to encrypt and decrypt anything you want pretty fast and easily. To use it in your code when you need to encrypt something or decrypt something. To encrypt everything in a specified folder to make sure people can't just snoop around easily. To bring you AES encryption without the hastle of setting everything up yourself. All you'll need to do is provide the information it asks for and it'll do all the work for you.

Feel free to ask me questions and stuff in the [Discussions](https://github.com/therealOri/oCrypt0r/discussions/14) page. <3
__ __
