import hashlib

#encode string
def encodeSHA512(string):
	hs =  hashlib.sha512()
	hs.update(string.encode("UTF-8"))
	hs = hs.hexdigest()
	return hs

#compare a strig with a hash
def testSHA512(string, hs):
	if encodeSHA512(str(string)) == hs:
		return True
	else:
		return False

#register an user
def regis(login, password):
	login = str(login)
	password = encodeSHA512(str(password))
	file = open("users.txt", 'a')
	file.write("\n"+login+"\n"+password)
	file.close()

print('''
	##################################################
        #             Secur Login v0.1 27/01/019         #
        #                  by alikhandkk81               #
        ##################################################

        [!] REGISTER ----> 1
        [!] LOGIN    ----> 2

	''')

op = int(input(">>> "))

if op == 1:
	#Register an user
	userName = input("Username: ")
	passWord = input("Password: ")
	passConf = input("Password: ")
	if passWord == passConf:
		try:
			regis(userName, passWord)
			print("\nSuccess!\n")
		except:
			print("\n;-; Fail... Try again\n")

else:
	userName = input("\nUsername: ")+"\n"
	passWord = input("Password: ")
	#open the "data base"
	with open("users.txt", 'r') as users:
		loginAndPass = users.readlines()
		#find for the login in "data base"
		if userName in loginAndPass:
			posi = loginAndPass.index(userName)
			#make the login
			if posi % 2 != 0:
				if testSHA512(passWord, loginAndPass[int(posi)+1].replace('\n', '')):
					print("\nSuccess!\n")
				else:
					print("\nInvalid login or password\n")
			else:
				print("\nInvalid login or password\n")
		else:
			print("\nInvalid login or password\n")
