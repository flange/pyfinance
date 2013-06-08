# encoding UTF-8

import getpass
import os
import hashlib

class Login:
	def __init__(self, max_auth_tries):
		self.max_auth_tries = max_auth_tries

	def userexists(self):
		"""
		Check if user exists.
		"""
		if (os.path.isfile("data/users")):
			return True
		else:
			return False


	def usercreate(self):
		"""
		Create new user.
		Write users (saves username and password hash)
		Write user_profile (saves all user information)
		Write user_profile_info (saves information for the programmer)
		"""
		print("Create a new user!")
		passwdkorrekt = 0
		while (passwdkorrekt == 0):
			users = input("Enter username: ")
			passwd = getpass.getpass("Enter password: ")
			passwdcheck = getpass.getpass("Repeat password: ")
			if (passwd == passwdcheck):
				passwdkorrekt = 1
			else:
				print("Password incorrect!\n"+
				      "Try again!")
		passwdhash = hashlib.md5(passwd.encode('utf-8'))
		passwdhexhash = passwdhash.hexdigest()
		userlogin_datei = open("data/users", "w")
		userlogin_datei.write(users +"\n"+passwdhexhash)
		userlogin_datei.close()
		userprofile_datei = open("data/"+users+"_profile", "w")
		userprofile_datei.write(users+"\n100000.00\n0")
		userprofileinfo_datei = open("data/"+users+"_profile_info", "w")
		userprofileinfo_datei.write("Username\nBudget\nDepotwert\n")
		print(users +" created sucessfully!")


	def authenticate(self):
		"""
		Check if user exists and password correct
		Read users
		"""
		count = 0
		print ("Login!")
		while(count < self.max_auth_tries):
			user = input("Username: ")
			passwd = getpass.getpass("Password: ")
			userlogin_datei = open("data/users", "r")
			datei_user = userlogin_datei.readline()
			datei_passwd = userlogin_datei.readline()
			datei_user_2 = datei_user[0:(len(datei_user)-1)]
			if (datei_user_2 == user):
				passwdhash = hashlib.md5(passwd.encode('utf-8'))
				passwdhexhash = passwdhash.hexdigest()
				if (passwdhexhash == datei_passwd):
					count = self.max_auth_tries
					print(">>Login successful!\n")
					return user
				else: print(">> Incorrect username or password!\n")
				count = count+1
			else:
				print(">> Incorrect username or password!")
				count = count+1
		userlogin_datei.close()


	def print_welcome(self):
		print ("Willkommen beim Boersenclient!\n")
