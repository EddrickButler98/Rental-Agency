import time
import fileinput
import os

print("Eddrick welcomes you to the MiTunes Music Rental Shop")
time.sleep(2)
print("Please feel free to choose wisely as we show you our in-stock albums!")
print("Please Wait.....")
time.sleep(3)
print(" ")
one_R = input("Are You Renting, Returning, or Replacing: ")
if one_R == "Replacing":
	replace = input("Which album do you want to replace(Format: 'Artist Name - Album Name')?: ")
	replacement_value = float(5.00)
	if replace == "Dangerous":
		artists_name = "Michael Jackson"
		renting_price = float(15.00)
		year_released = int(1991)
		sales_tax = float(0.07)

	elif replace == "The Birth of Soul":
		artists_name = "Ray Charles"
		renting_price = float(15.00)
		year_released = int(1991)
		sales_tax = float(0.07)

	elif replace == "The Carter V":
		artists_name = "Lil Wayne"
		renting_price = float(15.00)
		year_released = int(2017)
		sales_tax = float(0.07)

	elif replace == "Encore":
		artists_name = "Eminem"
		renting_price = float(20.00)
		year_released = int(2004)
		sales_tax = float(0.07)

	elif replace == "Stadium":
		artists_name = "Akon"
		renting_price = float(20.00)
		year_released = int(2015)
		sales_tax = 0.07

	replacing_with = input("With what?: ")
	if replacing_with == "Dangerous":
		artists_name = "Michael Jackson"
		renting_price = float(15.00)
		year_released = int(1991)
		sales_tax = float(0.07)

	elif replacing_with == "The Birth of Soul":
		artists_name = "Ray Charles"
		renting_price = float(15.00)
		year_released = int(1991)
		sales_tax = float(0.07)

	elif replacing_with == "The Carter V":
		artists_name = "Lil Wayne"
		renting_price = float(15.00)
		year_released = int(2017)
		sales_tax = float(0.07)

	elif replacing_with == "Encore":
		artists_name = "Eminem"
		renting_price = float(20.00)
		year_released = int(2004)
		sales_tax = float(0.07)

	elif replacing_with == "Stadium":
		artists_name = "Akon"
		renting_price = float(20.00)
		year_released = int(2015)
		sales_tax = 0.07

	with open('inventory.py', 'r+') as f:
    		content = f.read()
    		f.seek(0)
    		f.truncate()
    		f.write(content.replace(replace, replacing_with))
    		print("Replacements will cost $5.00, so you will be charged the replacement cost automatically for replacements!")
    		time.sleep(2)
	total = float(5.00)
	print('Cash Only')
	pay = int(input("Amount Being Paid: $"))
	change_left = float(pay) - float(total)
	time.sleep(2)
	print("Change Leftover:" + '${:0.2f}'.format(change_left))
	time.sleep(2)
	print("Thank you and please come back again!")
	receipt = open('replacements_log.py', 'a')
	receipt.write("\t\tReplaced " + str(replace) + " with " + str(replacing_with) + "\n")
	receipt.write("\t\tReplacement Price........" + '${:0.2f}'.format(total) + "\n")
	receipt.write("\t\tAmount Paid................." + '${:0.2f}'.format(pay) + "\n")
	receipt.write("\t\tChange Left..................." + '${:0.2f}'.format(change_left) + "\n")
	exit()

elif one_R == "Renting":
	while True:
		print(
			"\tMichael Jackson - Dangerous - Released in 1991 ---------- $15.00\n",
			"\tRay Charles - The Birth of Soul - Released in 1991 --------- $15.00\n",
			"\tLil Wayne - The Carter V - Upcoming 2017 Release -------- $20.00\n",
			"\tEminem - Encore - Released in 2004 ------------------------ $20.00\n",
			"\tAkon - Stadium - Released in 2015 -------------------------- $20.00\n")
		users_album = input("Which album do you want to rent?: ")
		if users_album == "Dangerous":
			artists_name = "Michael Jackson"
			renting_price = float(15.00)
			year_released = int(1991)
			sales_tax = float(0.07)
			number_of_days_renting = input("How many days are you renting " + users_album + " ?: ")
			break

		elif users_album == "The Birth of Soul":
			artists_name = "Ray Charles"
			renting_price = float(15.00)
			year_released = int(1991)
			sales_tax = float(0.07)
			number_of_days_renting = input("How many days are you renting " + users_album + " ?: ")
			break

		elif users_album == "The Carter V":
			artists_name = "Lil Wayne"
			renting_price = float(15.00)
			year_released = int(2017)
			sales_tax = float(0.07)
			number_of_days_renting = input("How many days are you renting " + users_album + " ?: ")
			break

		elif users_album == "Encore":
			artists_name = "Eminem"
			renting_price = float(20.00)
			year_released = int(2004)
			sales_tax = float(0.07)
			number_of_days_renting = input("How many days are you renting " + users_album + " ?: ")
			break

		elif users_album == "Stadium":
			artists_name = "Akon"
			renting_price = float(20.00)
			year_released = int(2015)
			sales_tax = 0.07
			number_of_days_renting = int(input("How many days are you renting " + users_album + " ?: "))
			if number_of_days_renting > 30:
				print("Maximum days to rent is 30 days! Pick Again!")

			else:
				print("Just a moment........")
				time.sleep(3)
				break

	invent = input("Do you want this in your inventory?: ")
	if invent == "yes":
		i = open('inventory.py', 'a')
		i.write("\t\t" + str(artists_name) + ' - ' + str(users_album) + "\n")
		i.close()

elif one_R == "Returning":
	while True:
		time.sleep(2)
		returned = input("Which album are you returning? (Notice: CHECK YOUR INVENTORY!): ")
		if str(returned) in open('inventory.py').read():
			for line in fileinput.input("inventory.py", inplace=True):
				if returned in line:
					continue
				print(line, end='')
			print("One moment please....")
			print("For Security Reasons:")
			artist = input("What was the artist's name?: ")
			year = input("What year was the album released?: ")
			time.sleep(2)
			print(
				"\t\tAlbum You're Returning............" + str(returned) + "\n",
				"\t\tArtist's Name.............................." + str(artist) + "\n",
				"\t\tAlbum Year Release..................." + str(year) + "\n"
				"\t\tCharge......................................." + '${:0.2f}'.format(0))
			time.sleep(2)
			print("Thank you for shopping with the MiTunes Family!")
			time.sleep(2)
			print("Have a nice day!")
			exit()
		else:
			print("You can't return an albums that's not in your inventory!")

print(" ")
payment_type = input("Cash, Credit, or Debit?: ")
if payment_type == "Cash":
	total = str(renting_price + sales_tax)
	print("Total: $" + str(total))
	users_paying = input("Amount You're Willing to Pay?(Format: '$50 or $50.00') : $")
	change = float(users_paying) - float(total)
	time.sleep(2)
	print("\t\tAlbum Name...................... " + str(users_album))
	print("\t\tArtist Name......................... " + str(artists_name))
	print("\t\tAlbum Renting Price......... " + '${:0.2f}'.format(renting_price))
	print("\t\tAmount Paid....................... $" + str(users_paying))
	print("\t\tChange Back....................... " + '${:0.2f}'.format(change))
	print("\t\tYear Released/Releasing..... Year " + str(year_released))
	print("\t\tNumber of Days Rented..." + str(number_of_days_renting) + " days")
	view_transactions = input("Would you like to view recent transactions: ")
	if view_transactions == "yes":
		with open('receipt.py', 'r') as receipts:
			for line in receipts:
				print(line)
	receipt = open('receipt.py', 'a')
	receipt.write("\t\tMiTunes Music Rental Shop\n\n")
	receipt.write("\t\tAlbum Name......................" + str(users_album) + "\n")
	receipt.write("\t\tArtist Name........................." + str(artists_name) + "\n")
	receipt.write("\t\tAlbum Renting Price......... " + '${:0.2f}'.format(renting_price) + "\n")
	receipt.write("\t\tAmount Paid...................... $" + str(users_paying) + "\n")
	receipt.write("\t\tTax....................................." + '${:0.2f}'.format(sales_tax) + "\n")
	receipt.write("\t\tChange Back......................" + '${:0.2f}'.format(change) + "\n")
	receipt.write("\t\tYear Released/Releasing....." + str(year_released) + "\n")
	receipt.write("\t\tDays Renting......................." + str(number_of_days_renting) + " days")
	receipt.write("\n\n")
	receipt.close()

elif payment_type == "Debit":
	print("We have different versions of debit cards, pick the one that's yours!")
	versions = input("Visa or MasterCard?: ")
	if versions == "Visa":
		number = input("Enter the last 4-digits of your VISA card number: ")
		pin = input("Please enter your PIN: ")
		time.sleep(2)
		print("Thank you for shopping with MiTunes!")
		print("Have a great day!")
		print("Album Name..................... " + str(users_album))
		print("Artist Name........................ " + str(artists_name))
		print("Album Renting Price........ " + '${:0.2f}'.format(renting_price))
		print("Year Released/Releasing.... Year " + str(year_released))
		print("Number of Days You Are Renting The Album For........ " + str(number_of_days_renting) + " days")
		view_transactions = input("Would you like to view recent transactions: ")
		if view_transactions == "yes":
			with open('receipt.py', 'r') as receipts:
				print("Just a minute.........")
				time.sleep(3)
				for line in receipts:
					print(line)
		receipt = open('receipt.py', 'a')
		receipt.write("\t\tMiTunes Music Rental Shop\n\n")
		receipt.write("\t\tAlbum Name......................" + str(users_album) + "\n")
		receipt.write("\t\tArtist Name........................." + str(artists_name) + "\n")
		receipt.write("\t\tAlbum Renting Price......... " + '${:0.2f}'.format(renting_price) + "\n")
		receipt.write("\t\tTax....................................." + '${:0.2f}'.format(sales_tax) + "\n")
		receipt.write("\t\tChange Back......................" + '${:0.2f}'.format(0) + "\n")
		receipt.write("\t\tYear Released/Releasing....." + str(year_released) + "\n")
		receipt.write("\t\tDays Renting......................." + str(number_of_days_renting) + " days")
		receipt.write("\n\n")
		receipt.close()

	elif versions == "MasterCard":
		number = input("Enter the last 4-digits of your MASTERCARD number: ")
		pin = input("Please enter your PIN: ")
		time.sleep(2)
		print("Thank you for shopping with MiTunes!")
		print("Have a great day!")
		print("Album Name..................... " + str(users_album))
		print("Artist Name........................" + str(artists_name))
		print("Album Renting Price......." + '${:0.2f}'.format(renting_price))
		print("Album's Release Year........" + str(year_released))
		print("Number of Days Rented..." + str(number_of_days_renting) + " days")
		view_transactions = input("Would you like to view recent transactions: ")
		if view_transactions == "yes":
			with open('receipt.py', 'r') as receipts:
				for line in receipts:
					print(line)
		receipt = open('receipt.py', 'a')
		receipt.write("\t\tMiTunes Music Rental Shop\n\n")
		receipt.write("\t\tAlbum Name......................" + str(users_album) + "\n")
		receipt.write("\t\tArtist Name........................." + str(artists_name) + "\n")
		receipt.write("\t\tAlbum Renting Price......... " + '${:0.2f}'.format(renting_price) + "\n")
		receipt.write("\t\tTax....................................." + '${:0.2f}'.format(sales_tax) + "\n")
		receipt.write("\t\tChange Back......................" + '${:0.2f}'.format(0) + "\n")
		receipt.write("\t\tYear Released/Releasing....." + str(year_released) + "\n")
		receipt.write("\t\tDays Renting......................." + str(number_of_days_renting) + " days")
		receipt.write("\n\n")
		receipt.close()

elif payment_type == "Credit":
	print("We also have different types of credit cards. Go ahead and tell which one is yours!")
	version = input("American Express, Discover, Capital One: ")
	if version == "American Express":
		number = input("Enter the last 4-digits of your American Express card number: ")
		pin = input("Please enter your PIN: ")
		print("Processing your transaction.....")
		time.sleep(3)
		print("Thank you for shopping with MiTunes!")
		print("Have a great day!")
		print("Album Name..................... " + str(users_album))
		print("Artist Name........................" + str(artists_name))
		print("Album Renting Price......." + '${:0.2f}'.format(renting_price))
		print("Album's Release Year........" + str(year_released))
		print("Number of Days Rented..." + str(number_of_days_renting) + " days")
		view_transactions = input("Would you like to view recent transactions: ")
		if view_transactions == "yes":
			with open('receipt.py', 'r') as receipts:
				for line in receipts:
					print(line)
		receipt = open('receipt.py', 'a')
		receipt.write("\t\tMiTunes Music Rental Shop\n\n")
		receipt.write("\t\tAlbum Name......................" + str(users_album) + "\n")
		receipt.write("\t\tArtist Name........................." + str(artists_name) + "\n")
		receipt.write("\t\tAlbum Renting Price......... " + '${:0.2f}'.format(renting_price) + "\n")
		receipt.write("\t\tTax....................................." + '${:0.2f}'.format(sales_tax) + "\n")
		receipt.write("\t\tChange Back......................" + '${:0.2f}'.format(0) + "\n")
		receipt.write("\t\tYear Released/Releasing....." + str(year_released) + "\n")
		receipt.write("\t\tDays Renting......................." + str(number_of_days_renting) + " days")
		receipt.write("\n\n")
		receipt.close()

	elif version == "Discover":
		number = input("Enter the last 4-digits of your Discover card number: ")
		pin = input("Please enter your PIN: ")
		print("Processing your transaction.........")
		time.sleep(2)
		print("Thanks you shopping with MiTunes!")
		print("Have a great day!")
		print("Album Name..................... " + str(users_album))
		print("Artist Name........................" + str(artists_name))
		print("Album Renting Price......." + '${:0.2f}'.format(renting_price))
		print("Album's Release Year........" + str(year_released))
		print("Number of Days Rented..." + str(number_of_days_renting) + " days")
		view_transactions = input("Would you like to view recent transactions: ")
		if view_transactions == "yes":
			with open('receipt.py', 'r') as receipts:
				for line in receipts:
					print(line)
		receipt = open('receipt.py', 'a')
		receipt.write("\t\tMiTunes Music Rental Shop\n\n")
		receipt.write("\t\tAlbum Name......................" + str(users_album) + "\n")
		receipt.write("\t\tArtist Name........................." + str(artists_name) + "\n")
		receipt.write("\t\tAlbum Renting Price......... " + '${:0.2f}'.format(renting_price) + "\n")
		receipt.write("\t\tTax....................................." + '${:0.2f}'.format(sales_tax) + "\n")
		receipt.write("\t\tChange Back......................" + '${:0.2f}'.format(0) + "\n")
		receipt.write("\t\tYear Released/Releasing....." + str(year_released) + "\n")
		receipt.write("\t\tDays Renting......................." + str(number_of_days_renting) + " days")
		receipt.write("\n\n")
		receipt.close()

	elif version == "Capital One":
		number = input("Enter the last 4-digits of your Capital One card number: ")
		pin = input("Please enter your PIN: ")
		print("Processing your transaction.........")
		time.sleep(2)
		print("Thank you for shopping with MiTunes!")
		print("Have a great day!")
		print("Album Name..................... " + str(users_album))
		print("Artist Name........................" + str(artists_name))
		print("Album Renting Price......." + '${:0.2f}'.format(renting_price))
		print("Album's Release Year........" + str(year_released))
		print("Number of Days Rented..." + str(number_of_days_renting) + " days")
		view_transactions = input("Would you like to view recent transactions: ")
		if view_transactions == "yes":
			with open('receipt.py', 'r') as receipts:
				for line in receipts:
					print(line)
		receipt = open('receipt.py', 'a')
		receipt.write("\t\tMiTunes Music Rental Shop\n\n")
		receipt.write("\t\tAlbum Name......................" + str(users_album) + "\n")
		receipt.write("\t\tArtist Name........................." + str(artists_name) + "\n")
		receipt.write("\t\tAlbum Renting Price......... " + '${:0.2f}'.format(renting_price) + "\n")
		receipt.write("\t\tTax....................................." + '${:0.2f}'.format(sales_tax) + "\n")
		receipt.write("\t\tChange Back......................" + '${:0.2f}'.format(0) + "\n")
		receipt.write("\t\tYear Released/Releasing....." + str(year_released) + "\n")
		receipt.write("\t\tDays Renting......................." + str(number_of_days_renting) + " days")
		receipt.write("\n\n")
		receipt.close()
