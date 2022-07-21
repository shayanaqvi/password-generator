import time
import random
from os import *

def get_password_length():
	time.sleep(0.5)
	password_length = input("\nHow many characters should your new password be? ")

	if password_length.isdigit() == False:
		print("\nHey! That's not a number!")
		system('exit')
	elif int(password_length) <= 7:
		print("Hmmmmmmmmmmm...")
		time.sleep(0.75)
		print("That's not long enough. A good password is at least 8 characters.")
		time.sleep(0.75)
		system('exit')
	elif password_length.isdigit() == True:
		generate_password(password_length)

def generate_password(password_length):

	letters = ["a", "b", "c", "d", "e", "f", 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	special_chars = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", ";", ":", "<", "|", ">", "?", "/"]

	password = []

	increment = 0

	print("\nYour new password is: ")

	while increment <= (int(password_length) - 1):
		increment += 1
		select_character = random.randint(0, 2)

		if select_character == 0:
			password = letters[random.randint(0, 25)]
		elif select_character == 1:
			password = numbers[random.randint(0, 9)]
		elif select_character == 2:
			password = special_chars[random.randint(0, 23)]

		print(password, end='')

	print("\n\nKeep it safe!")
	time.sleep(0.5)

get_password_length()

print("")
