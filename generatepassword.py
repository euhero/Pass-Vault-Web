import hashlib
import base64



def GeneratePass(masterpassword,username,website):

	genpassword = f'({website}|{username}|{masterpassword})'
	genpassword = hashlib.sha1(genpassword.encode()).hexdigest()
	genpassword = base64.b64encode(genpassword.encode())
	genpassword = genpassword.decode()[:12]

	return genpassword


if __name__ == "__main__":
	masterpassword = 'Cypher384376!'
	username = 'euhero'
	website = 'facebook.com'
	GeneratePass(masterpassword,username,website)

