from cryptography.fernet import Fernet

#DEKRIPSI

key = open('filekey.key', 'rb').read()
# pakai kunci yang tadi
fernet = Fernet(key)

# buka file hasil enkrpisi
with open('encrypted.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

# langsung di dekripsi 
decrypted = fernet.decrypt(encrypted)

# cek hasil dekripsi cocok apa tidak ??
with open('decrypted.csv', 'wb') as dec_file:
	dec_file.write(decrypted)