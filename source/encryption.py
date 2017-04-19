from passlib.hash import pbkdf2_sha256
from passlib import pwd
from gui import DATBOI
from init import logger

#password = pwd.genword(length=13, charset="ascii_62")
password = "thisisapassword"
print (password)

hash = pbkdf2_sha256.hash(password)
print (hash)

print(pbkdf2_sha256.verify(password, hash))
print(pbkdf2_sha256.verify("AYYYYY LMAO", hash))