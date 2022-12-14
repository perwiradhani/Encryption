from Crypto.PublicKey import RSA

# keyPair = RSA.generate(1024)
# print(keyPair)

publicKey = RSA.generate(1024)

with open('publicKey.pem', 'wb') as p:
    p.write(publicKey.exportKey('PEM'))
# with open('privateKey.pem', 'wb') as p:
#     p.write(privateKey.save_pkcs1('PEM'))