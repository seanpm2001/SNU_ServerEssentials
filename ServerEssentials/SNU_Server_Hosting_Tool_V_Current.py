# SNU server essentials
'''
Server hosting tool
Use this tool to host your own SNU server
This program has all the tools for hosting your SNU server
'''
print ("SNU Server Essentials - Server Host tool")
print ("Host your SNU server with this tool")
startup1 = input("\nPress [ENTER] key to start")
print ("Setup part 1")
accountAsk1 = str(input("Do you want to use an existing account? Y/N"))
accountAsk1 == accountAsk1.upper
# if (accountAsk1 != "Y" and accountAsk1 != "N"):
if (accountAsk1 != "Y"):
	if (accountAsk1 != "N"):
		print ("Invalid input entered!")
		print ("Setup aborted")
		crash1 = input("Press [ENTER] key to close")
		craVar1 = int(3)
		craVar2 = float(4.1)
		craAns1 = int(craVar1 + craVar2)
		print (str(craAns1))
if (accountAsk1 == "Y"):
	print ("Searching for an existing account...")
	print ("ERROR: Cannot find an existing account. Server hosting tool is too old")
	noMore = input("Press [ENTER] key to quit")
if (accountAsk1 == "N"):
	print ("Account setup")
	username1 = str(input("Enter a username: "))
	password1 = str(input("Enter a password (at least 16 characters): "))
	confirmPassword1 = str(input("Confirm your password: "))
	if (len.password1 > 16):
		print ("Password must be at least 16 characters")
	if (confirmPassword1 == password1):
		print ("Successfully logged in")
	else:
		print ("ERROR: INVALID PASSWORD")
noMore = input("Press [ENTER] key to quit")
print ("")