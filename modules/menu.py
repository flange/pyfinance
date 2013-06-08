# encoding: UTF-8

import sys
import os

import modules.buy as buy

class Menu:
	"""
	Displays the menu after login.
	There you can select your preferred option
	"""

	def __init__(self):
		self.pos_options = ['y', 'yes']
		self.neg_options = ['n', 'no']


	def get_input(self):
		userinput = input()
		sys.stdout.write("\033[F \b\n")  # delete the values typed to chose
		return userinput


	def printmenu(self):
		"""
		Prints the menu
		implements the switch case of the other options
		"""
		print("Menu:")
		print("[0] Print Menu")
		print("[1] Budget")
		print("[2] Open Depot")
		print("[3] Buy stocks")
		print("[4] Sell stocks")
		print("[5] Statistics")
		print("[6] Logout")


	def option_budget(self, registered_user):
		"""
		Shows your cash
		"""
		if not (os.path.isfile("data/"+registered_user+"_profile")):
			print("Something wrong, no userprofilfile found")
			return

		profile_file = open("data/"+registered_user+"_profile", "r")

		lines  = profile_file.readlines()
		budget = lines[1]  # 2nd row contains budget

		profile_file.close()
		print ("Budget: "+ budget)


	def option_depot(self):
		"""
		Shows your stock depot
		"""
		pass

	def option_buy_companycheck(self, stockname):
		print(">> Companycheck!")
		return True


	def option_buy_moneycheck(self, stockname, amount):
		print(">> Moneycheck!")
		return True


	def option_buy(self, user):
		"""
		Gives you the option to buy stocks
		"""
		finished = False
		exists = False
		enoughmoney = False
		verification = False

		stockdata = open("data/dax_data", "r")
		# Here: Reading the file into a nice datastructure!

		while not finished:
			stockname = input(">> Please enter the company from which to buy from: ")
			exists = self.option_buy_companycheck(stockname)
			if exists == True:
				amount = input(">> Please enter how many stocks you want to buy: ")
				enoughmoney = self.option_buy_moneycheck(stockname, amount)
				if enoughmoney == True:
					verification = input(">> Do you really want to buy "+amount+" of "+stockname+"? [Y][N]")
					if (verification == 'y' or verification == 'Y'):
						print (">> Successfully transaction!")
					elif (verification == 'n' or verification == 'N'):
						print (">> No transaction verification, please try again!")
					else:
						print (">>User abort, please try again!")
				else:
					print(">> You have not enough money to buy " +amount+ " of " +stockname+ ", please try again!")
			else:
				print(">> Company does not exist, please try again!")

			again = input(">> Do you want buy more? [Y][N]")
			if (again == 'y' or again == 'Y'):
				finished = Falseregistered_user
			else:
				finished = True

		stockdata.close()


	def buy(self, user, data_dir, data_file_path, thread_lock, company_names):

		op_buy = buy.Buy(user, data_dir, data_file_path, thread_lock, company_names)

		while True:
			company = op_buy.get_company_name()

			if (company is None):
				self.printmenu()
				break

			amount  = op_buy.get_amount_of_stock()

			if (amount is None):
				self.printmenu()
				break

			print(company, amount)

			#op_buy.transaction(company, amount, user)




	def option_sell(self):
		"""
		Gives you the option to sell stocks
		"""


	def option_statistics(self):
		"""
		Shows you statistics about all the other players
		Updated weekly
		"""


	def option_logout(self, state):
		"""
		Logout the user and exit the program!
		must synchronize all open files, save and close them
		"""
		state.running = False



