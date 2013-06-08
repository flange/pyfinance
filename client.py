#!/usr/bin/env python

import os
import threading

import modules.logger   as logger
import modules.fetcher  as fetcher
import modules.login    as login
import modules.menu     as menu
import modules.helper   as helper

# create necessary directory structure if it doesn't exist already
working_dir = os.getcwd()

data_dir = working_dir + "/data"
if not os.path.exists(data_dir):
	os.mkdir("data")

log_dir = working_dir + "/log"
if not os.path.exists(log_dir):
	os.mkdir("log")


# global thread lock
thread_lock = threading.Lock()

# global program state
state = helper.Bool_Wrapper()
state.running = True


# LOGIN
max_auth_tries = 3
client_login   = login.Login(max_auth_tries)

client_login.print_welcome()

if client_login.userexists():
	registered_user = client_login.authenticate()
else:
	client_login.usercreate()
	registered_user = client_login.authenticate()



# FETCH DAX DATA
url = "http://de.finance.yahoo.com/d/quotes.csv?s=@%5EGDAXI&f=sa&"
client_fetcher = fetcher.Fetcher(url, data_dir, "dax_data", log_dir, "fetch.log")
poll_interval_sec = 60

# start fetch thread to poll dax data
fetch_thread = threading.Thread(target=client_fetcher.fetch_dax_data, args=(poll_interval_sec, thread_lock))
fetch_thread.daemon = True

fetch_thread.start()


# MAIN MENU
menu = menu.Menu()
menu.printmenu()


while state.running is True:

	option = menu.get_input()

	if (option == '0'):
		option_thread = threading.Thread(target = menu.printmenu)
		option_thread.daemon = True
		option_thread.start()
		option_thread.join()

	elif (option == '1'):
		print("Choosed option: Budget")
		option_thread = threading.Thread(target = menu.option_budget, args=(registered_user,))
		option_thread.daemon = True
		option_thread.start()
		option_thread.join()

	elif (option == '2'):
		print ("Choosed option: Depot")
		option_thread = threading.Thread(target = menu.option_depot)
		option_thread.daemon = True
		option_thread.start()
		option_thread.join()

	elif (option == '3'):
		print ("Choosed option: Buy")
		option_thread = threading.Thread(target = menu.option_buy, args=(registered_user,))
		option_thread.daemon = True
		option_thread.start()
		option_thread.join()

	elif (option == '4'):
		print ("Choosed option: Sell")
		option_thread = threading.Thread(target = menu.option_sell)
		option_thread.daemon = True
		option_thread.start()
		option_thread.join()

	elif (option == '5'):
		print ("Choosed option: Statistics")
		option_thread = threading.Thread(target = menu.option_statistics)
		option_thread.daemon = True
		option_thread.start()
		option_thread.join()

	elif (option == '6'):
		print ("Choosed option: Logout")
		option_thread = threading.Thread(target = menu.option_logout, args=(state,))
		option_thread.daemon = True
		option_thread.start()
		option_thread.join()

	else:
		print ("Wrong input, try again!\n")
		option = menu.printmenu()



option_thread.join()
