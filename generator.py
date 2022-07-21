import time
import random

def generate_password():
	
	password_length = input("How long should your new password be? ")

	letters = ["a", "b", "c", "d", "e", "f", 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	special_chars = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", ";", ":", "<", "|", ">", "?", "/"]

	password = []

	increment = 0

	while increment <= int(password_length):
		increment += 1
		select_character = random.randint(0, 2)

		if select_character == 0:
			password = letters[random.randint(0, 25)]
		elif select_character == 1:
			password = numbers[random.randint(0, 9)]
		elif select_character == 2:
			password = special_chars[random.randint(0, 23)]

		print(password, end='')

generate_password()
print("")
