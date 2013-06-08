import os
import modules.helper as helper

class Buy:
	def __init__(self, user, data_dir, data_file_path, thread_lock, company_names):
		self.user      = user
		self.data_file = data_file_path
		self.data_dir  = data_dir
		self.dax_data  = helper.parse_dax_data(data_file_path, thread_lock)
		self.lock      = thread_lock
		self.companies = company_names


	def get_company_name(self):

		companies = self.get_company_list()

		while True:
			company = input("Enter company:\n")

			if company == 'list':
				print("\nAvailable companies:")

				for c in companies:
					comp_name = self.companies[c]
					print('{0:8} {1}'.format(c, comp_name))

				print("\n", end="")
				continue

			if company == 'cancel':
				print("\n", end="")
				return None

			if company not in companies:
				print("Unknown company. Please enter a valied company.")
				print("Enter 'list' for a list of available companies or 'cancel' to leave\n")

			if company in companies:
				self.buy_company = company
				print("\n", end="")
				return company


	def get_amount_of_stock(self):

		company  = self.buy_company

		comp_val = self.dax_data[company]
		comp_val = helper.float_string_to_int(comp_val)


		# get profile budget
		usr_profile = self.data_dir + '/' + self.user + "_profile"

		if not (os.path.isfile(usr_profile)):
			print("Couldn't read user profile to get user cash")
			return None

		profile_file = open(usr_profile, "r")
		lines  = profile_file.readlines()
		profile_file.close()

		user_cash = helper.float_string_to_int(lines[1])


		while True:
			amount = input("Enter amount:\n")

			if (amount == "cancel"):
				print("\n", end="")
				return None

			if (not amount.isdigit()):
				print("Please enter a valid amount of stocks or 'cancel' to leave\n")
				continue

			amount = int(amount)


			price = amount * comp_val

			if (user_cash < price):
				float_price = helper.int_to_float_string(price)
				float_cash  = helper.int_to_float_string(user_cash)

				print("\n", end="")
				print("Insufficient funds.")
				print("You need:    {0}€".format(float_price))
				print("Your budget: {0}€".format(float_cash))
				print("\n", end="")
				continue


			self.amount = amount
			self.comp_val = comp_val

			return amount


	def transaction(self, company, amount, user):
		pass


	def get_company_list(self):
		companies = list(self.dax_data.keys())
		companies.sort()

		return companies
