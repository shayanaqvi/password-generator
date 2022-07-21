import time
import random

def generate_password():
	
	password_length = input("How long should your new password be? ")

	letters = ["a", "b", "c", "d", "e", "f", 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

	for i in range(0, int(password_length)):
		print(letters[random.randint(0, 25)], end='')
		print(numbers[random.randint(0, 9)], end='')
	print("")

generate_password()
