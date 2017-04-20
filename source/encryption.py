from passlib.hash import pbkdf2_sha512
from passlib import pwd

"""#Define or generate a password
#password = pwd.genword(length=13, charset="ascii_62")
password = "thisisapasswordlol"
print (password)

#Hash the password, the function also generates and adds a salt
hash = pbkdf2_sha512.hash(password)
print (hash)

#Attempt to verify the password
print(pbkdf2_sha512.verify(password, hash))
print(pbkdf2_sha512.verify("AYYYYY LMAO", hash))"""

def setPassword(password):
    if len(password) >= 14 and len(password) <= 20:
        hash = pbkdf2_sha512.hash(password)
    else:
        return self.set_error(field, self.VALIDATION_ERRORS["ERR_LENGTH"]) 

def verifyClientKey(key):
    if pbkdf2_sha512.verify(key, hash) == true:
        print("It's a match!")
    else:
        print("Wrong password!")