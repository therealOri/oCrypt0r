import base64
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


    def string_encrypt(self, string, enc_key, enc_salt):

        key = PBKDF2(enc_key, enc_salt, dkLen=32)
        rb = get_random_bytes(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, rb)
        cipher_data = base64.b64encode(rb + cipher.encrypt(pad(string.encode('utf-8'), AES.block_size)))
        return cipher_data.decode()


    def string_decrypt(self, string, enc_key, enc_salt):
        b64d = base64.b64decode(string)

        try:
            key = PBKDF2(enc_key, enc_salt, dkLen=32)
            cipher = AES.new(key, AES.MODE_CBC, b64d[:AES.block_size])
            d_cipher_data = unpad(cipher.decrypt(b64d[AES.block_size:]), AES.block_size)
        except Exception as e:
            strd_e = f'The provided "enc_salt" or the "enc_key" does not match what was was used to encrypt the data...\nError: {e}'
            raise Exception(strd_e) from None
        return d_cipher_data.decode()




    def file_encrypt(self, file, enc_key, enc_salt):
        BUF_SIZE = 65536
        isFile = os.path.isfile(file)
        if isFile == True:
            key = PBKDF2(enc_key, enc_salt, dkLen=32)
            rb = get_random_bytes(AES.block_size)
            cipher = AES.new(key, AES.MODE_CBC, rb)
            
            with open(file, 'rb') as f:
                while True:
                    data = f.read(BUF_SIZE)
                    if not data:
                        break
                    try:
                        cipher_data = base64.b64encode(rb + cipher.encrypt(pad(data, AES.block_size)))
                    except Exception as e:
                        raise Exception(e)

            try:
                with open(file, 'wb') as f2:
                    f2.write(cipher_data)
                    os.rename(file, f'{file}.oCrypted')
            except Exception:
                flee_e2 = "Could not open, write into, or replace/rename the file.  |  File may have no data to encrypt."
                raise Exception(flee_e2) from None
            
        else:
            m = 'File not found...The provided file is either a directory/folder, spelled incorrectly, or does not exist where specified.'
            raise Exception(m)
            

    
    def file_decrypt(self, file, enc_key, enc_salt):
        isFile = os.path.isfile(file)
        if isFile == True:
            if file.endswith('.oCrypted'):
                with open(file, 'rb') as f:
                    string = f.read()
                    if not string:
                        fled_e = "File is empty..nothing to decrypt"
                        raise Exception(fled_e) from None
                    if string == b'':
                        fled_e2 = "File is empty..nothing to decrypt"
                        raise Exception(fled_e2) from None
                    elif string == '':
                        fled_e3 = "File is empty..nothing to decrypt"
                        raise Exception(fled_e3) from None
                    else:
                        b64d = base64.b64decode(string)
                        try:
                            key = PBKDF2(enc_key, enc_salt, dkLen=32)
                            cipher = AES.new(key, AES.MODE_CBC, b64d[:AES.block_size])
                            d_cipher_data = unpad(cipher.decrypt(b64d[AES.block_size:]), AES.block_size)
                        except Exception as e:
                            fled_e3 = f'The provided "enc_salt" or the "enc_key" does not match what was was used to encrypt the data...\nError: {e}'
                            raise Exception(fled_e3) from None
                    try:
                        with open(file, 'wb') as f2:
                            f2.write(d_cipher_data)
                            os.rename(file, file.replace('.oCrypted', ''))
                    except Exception:
                        fled_e4 = "Could not open, write into, or replace/rename the file.."
                        raise Exception(fled_e4) from None
            else:
                pass
        else:
            m = 'File not found...The provided file is either a directory/folder, spelled incorrectly, or does not exist where specified.'
            raise Exception(m)


    












    #These following functions are meant to be used repeatedly by the directory encryption.
    # They do not have any errors that will raise, They do not return anything, They are not meant to be used for one file only. file_encrypt() is meant for that.

    # FOR dir_encrypt() ONLY!
    def fdir_enc(self, file, enc_key, enc_salt):
        BUF_SIZE = 65536
        isFile = os.path.isfile(file)
        if isFile == True:
            key = PBKDF2(enc_key, enc_salt, dkLen=32)
            rb = get_random_bytes(AES.block_size)
            cipher = AES.new(key, AES.MODE_CBC, rb)

            with open(file, 'rb') as f:
                while True:
                    data = f.read(BUF_SIZE)
                    if not data:
                        break
                    elif data == '':
                        break
                    else:
                        cipher_data = base64.b64encode(rb + cipher.encrypt(pad(data, AES.block_size)))
                        with open(file, 'wb') as f2:
                            f2.write(cipher_data)
                            os.rename(file, f'{file}.oCrypted')
                        break
        else:
            m = 'File not found...The provided file is either a directory/folder, spelled incorrectly, or does not exist where specified.'
            raise Exception(m)


    # FOR dir_decrypt() ONLY!
    def fdir_dcr(self, file, enc_key, enc_salt):
        isFile = os.path.isfile(file)
        if isFile == True:
            if file.endswith('.oCrypted'):
                with open(file, 'rb') as f:
                    string = f.read()
                    if not string:
                        pass
                    elif string == b'':
                        pass
                    elif string == '':
                        pass
                    else:
                        b64d = base64.b64decode(string)
                        key = PBKDF2(enc_key, enc_salt, dkLen=32)
                        cipher = AES.new(key, AES.MODE_CBC, b64d[:AES.block_size])
                        d_cipher_data = unpad(cipher.decrypt(b64d[AES.block_size:]), AES.block_size)

                        with open(file, 'wb') as f2:
                            f2.write(d_cipher_data)
                            os.rename(file, file.replace('.oCrypted', ''))

            else:
                pass
        else:
            flD_m = 'File not found...The provided file is either a directory/folder, spelled incorrectly, or does not exist where specified.'
            raise Exception(flD_m)



    def dir_encrypt(self, dir_path, enc_key, enc_salt):
        isDirectory = os.path.isdir(dir_path)
        if isDirectory == True:
            for path, subdirs, files in os.walk(dir_path):
                for name in files:
                    try:
                        self.fdir_enc(f'{path}/{name}', enc_key, enc_salt)
                    except Exception as ee:
                        raise Exception(ee) from None
        else:
            dirm = 'Directory not found...The provided directory/folder is either a file, spelled incorrectly, or does not exist where specified.'
            raise Exception(dirm)

    def dir_decrypt(self, dir_path, enc_key, enc_salt):
        isDirectory = os.path.isdir(dir_path)
        if isDirectory == True:
            for path, subdirs, files in os.walk(dir_path):
                for name in files:
                    try:
                        self.fdir_dcr(f'{path}/{name}', enc_key, enc_salt)
                    except Exception as ed:
                        raise Exception(ed) from None
        else:
            dirm2 = 'Directory not found...The provided directory/folder is either a file, spelled incorrectly, or does not exist where specified.'
            raise Exception(dirm2)


        
        
