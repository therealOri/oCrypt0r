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

    def __init__(self):
        self.hash_key = hashlib.blake2b(bytes('theralOri', 'utf-8'), digest_size=16, salt=bytes('dykGihgkHgYJgfuG', 'utf-8')).digest()


    def clear(self):
        os.system('clear||cls')


    def string_encrypt(self, string, salt):
        key = PBKDF2(self.hash_key, salt, dkLen=32)
        rb = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, rb)
        cipher_data = base64.b64encode(rb + cipher.encrypt(pad(string.encode('utf-8'), AES.block_size)))
        self.clear()
        return cipher_data.decode()


    def string_decrypt(self, string, salt):
        FLAG1 = True
        b64d = base64.b64decode(string)

        try:
            key = PBKDF2(self.hash_key, salt, dkLen=32)
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


    def file_encrypt(self, file, salt):
        BUF_SIZE = 65536
        
        key = PBKDF2(self.hash_key, salt, dkLen=32)
        rb = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, rb)

        with open(file, 'r+b') as f:
            while True:
                data = f.read(BUF_SIZE)
                if not data:
                    break
                cipher_data = base64.b64encode(rb + cipher.encrypt(pad(data, AES.block_size)))
        with open(file, 'wb') as f2:
            f2.write(cipher_data)
            os.rename(file, f'{file}.oCrypted')
        return

    
    def file_decrypt(self, file, salt):
        FLAG2 = True
        with open(file, 'rb') as f:
            string = f.read()
            b64d = base64.b64decode(string)

            try:
                key = PBKDF2(self.hash_key, salt, dkLen=32)
                cipher = AES.new(key, AES.MODE_CBC, b64d[:AES.block_size])
                d_cipher_data = unpad(cipher.decrypt(b64d[AES.block_size:]), AES.block_size)
            except Exception as e:
                self.clear()
                print(f'Oops..An error has occured. Please try again.\nError: {e}\n\n')
                input('Press "Enter" to contine...')
                self.clear()
                FLAG2 = False

        with open(file, 'wb') as f2:
            f2.write(d_cipher_data)
            os.rename(file, file.replace('.oCrypted', ''))
        
        if FLAG2 == True:
            return True
        elif FLAG2 == False:
            return False
