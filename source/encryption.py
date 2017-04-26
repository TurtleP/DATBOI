from passlib.hash import pbkdf2_sha512

def setPassword(password):
	if len(password) >= 14 and len(password) <= 20:
		return pbkdf2_sha512.hash(password)

def verifyClientKey(key, hash):
	if pbkdf2_sha512.verify(key, hash):
		print("It's a match!")
	else:
		print("Wrong password!")

print(setPassword("ayylmaotopkek!"))

try:
	print(verifyClientKey("ayylmaotopkek!", "$pbkdf2-sha512$25000$DkHIee.9F6J0LiVEqPW.9w$DqKp0oHPKCdU4geQFwWl8XLZHBuroUdxhP4lv7B0tuOgTH9dspsA.Mhs9GaiZXVcrgAftQ6RctwbXV/cWbzdSQ"))
except ValueError:
	print("not valid")