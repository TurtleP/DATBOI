from passlib.hash import pbkdf2_sha256
from passlib import pwd
from gui import DATBOI
from init import logger

#Define or generate a password
#password = pwd.genword(length=13, charset="ascii_62")
password = "thisisapassword"
print (password)

#Hash the password, the function also generates and adds a salt
hash = pbkdf2_sha256.hash(password)
print (hash)

#Attempt to verify the password
print(pbkdf2_sha256.verify(password, hash))
print(pbkdf2_sha256.verify("AYYYYY LMAO", hash))