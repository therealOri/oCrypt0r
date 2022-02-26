import base64
import hashlib
import sys
import time
import os
from halo import Halo

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
        self.hash_key = hashlib.blake2b('theralOri'.encode('utf-8'), digest_size=16, salt=bytes('dykGihgkHgYJgfuG', 'utf-8')).digest()


    def clear(self):
        os.system('clear||cls')

    
    def ESpin(self):
        self.clear()
        spinner = Halo(text='Encrypting..', spinner='dots', placement='right')
        spinner.start()
        time.sleep(2.5)
        spinner.stop()


    def DSpin(self):
        self.clear()
        spinner = Halo(text='Decrypting..', spinner='dots', placement='right')
        spinner.start()
        time.sleep(2.5)
        spinner.stop()


    def Encrypt(self, string, salt):
        key = PBKDF2(self.hash_key, salt, dkLen=32)
        rb = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, rb)
        cipher_data = base64.b64encode(rb + cipher.encrypt(pad(string.encode('utf-8'), AES.block_size)))
        self.ESpin()
        self.clear()
        return cipher_data.decode()


    def Decrypt(self, string, salt):
        FLAG = True
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
            FLAG = False
        if FLAG == True:
            self.DSpin()
            self.clear()
            return d_cipher_data.decode()
        else:
            return None
