import time
import random

def generate_password():
	
	password_length = input("How long should your new password be? ")

	letters = ["a", "b", "c", "d", "e", "f"]
	numbers = [1, 2, 3, 4, 5, 6]

	for i in range(0, int(password_length)):
		print(letters[random.randint(0, 5)], end='')

	print("")

generate_password()
