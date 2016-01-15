
import base64
import md5
import os
from Crypto.Cipher import AES

    
def decrypt_password():
	pwdBase64 = base64.b64decode("Put yourpasword here")
        iv = pwdBase64[:16]
        encryptDigest = pwdBase64[16:]
        decryptor = AES.new(md5.new("mR3m").digest(), AES.MODE_CBC, iv)
        password = decryptor.decrypt(encryptDigest)
        if len(password)>0 and (ord(password[-1]) < 33 or ord(password[-1]) > 126):
            password = password.strip(password[-1])
	print password 

decrypt_password()
