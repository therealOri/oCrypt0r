import base64
import hashlib
import sys
import time
import os

#AES Fun##
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
##-------##

# main.py
# Date: 02/24/2022
# Author: therealOri



class oCrypt:


    def clear(self):
        os.system('clear||cls')


    def string_encrypt(self, key, key_salt, string, string_salt):
        hash_key = hashlib.blake2b(bytes(key, 'utf-8'), digest_size=16, salt=bytes(key_salt, 'utf-8')).digest()

        key = PBKDF2(hash_key, string_salt, dkLen=32)
        rb = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, rb)
        cipher_data = base64.b64encode(rb + cipher.encrypt(pad(string.encode('utf-8'), AES.block_size)))
        self.clear()
        return cipher_data.decode()


    def string_decrypt(self, key, key_salt, string, string_salt):
        FLAG1 = True
        hash_key = hashlib.blake2b(bytes(key, 'utf-8'), digest_size=16, salt=bytes(key_salt, 'utf-8')).digest()
        b64d = base64.b64decode(string)

        try:
            key = PBKDF2(hash_key, string_salt, dkLen=32)
            cipher = AES.new(key, AES.MODE_CBC, b64d[:AES.block_size])
            d_cipher_data = unpad(cipher.decrypt(b64d[AES.block_size:]), AES.block_size)
        except Exception as e:
            self.clear()
            print(f'Oops..An error has occured. Please try again.\nError: {e}\n\n')
            input('Press "Enter" to contine...')
            self.clear()
            FLAG1 = False
        if FLAG1 == True:
            self.clear()
            return d_cipher_data.decode()
        else:
            return None


    def file_encrypt(self, key, key_salt, file, file_salt):
        BUF_SIZE = 65536
        hash_key = hashlib.blake2b(bytes(key, 'utf-8'), digest_size=16, salt=bytes(key_salt, 'utf-8')).digest()
        isFile = os.path.isfile(file)
        if isFile == True:
            key = PBKDF2(hash_key, file_salt, dkLen=32)
            rb = get_random_bytes(AES.block_size)
            cipher = AES.new(key, AES.MODE_CBC, rb)
            try:
                with open(file, 'rb') as f:
                    while True:
                        data = f.read(BUF_SIZE)
                        if not data:
                            break
                        cipher_data = base64.b64encode(rb + cipher.encrypt(pad(data, AES.block_size)))
                with open(file, 'wb') as f2:
                    f2.write(cipher_data)
                    os.rename(file, f'{file}.oCrypted')
            except Exception as e:
                return False
            return True
        else:
            return False

    
    def file_decrypt(self, key, key_salt, file, file_salt):
        hash_key = hashlib.blake2b(bytes(key, 'utf-8'), digest_size=16, salt=bytes(key_salt, 'utf-8')).digest()
        isFile = os.path.isfile(file)
        if isFile == True:
            try:
                with open(file, 'rb') as f:
                    string = f.read()
                    b64d = base64.b64decode(string)
                    try:
                        key = PBKDF2(hash_key, file_salt, dkLen=32)
                        cipher = AES.new(key, AES.MODE_CBC, b64d[:AES.block_size])
                        d_cipher_data = unpad(cipher.decrypt(b64d[AES.block_size:]), AES.block_size)
                    except Exception as e:
                        self.clear()
                        print(f'Oops..An error has occured. Please try again.\nError: {e}\n\n')
                        input('Press "Enter" to contine...')
                        self.clear()
                with open(file, 'wb') as f2:
                    f2.write(d_cipher_data)
                    os.rename(file, file.replace('.oCrypted', ''))
            except Exception as e:
                return False
            return True
        else:
            return False




    def dir_encrypt(self, key, key_salt, dir_path, dir_salt):
        hash_key = hashlib.blake2b(bytes(key, 'utf-8'), digest_size=16, salt=bytes(key_salt, 'utf-8')).digest()
        isDirectory = os.path.isdir(dir_path)
        if isDirectory == True:
            BUF_SIZE = 65536
            for path, subdirs, files in os.walk(dir_path):
                for name in files:
                    try:
                        self.file_encrypt(key, key_salt, f'{path}/{name}', dir_salt)
                    except Exception as e:
                        return False
                return True
        else:
            return False

    def dir_decrypt(self, key, key_salt, dir_path, dir_salt):
        hash_key = hashlib.blake2b(bytes(key, 'utf-8'), digest_size=16, salt=bytes(key_salt, 'utf-8')).digest()
        isDirectory = os.path.isdir(dir_path)
        if isDirectory == True:
            BUF_SIZE = 65536
            for path, subdirs, files in os.walk(dir_path):
                for name in files:
                    try:
                        self.file_decrypt(key, key_salt, f'{path}/{name}', dir_salt)
                    except Exception as e:
                        return False
                return True
        else:
            return False


        
        
