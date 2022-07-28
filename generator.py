import time
import random
from tkinter import *
from os import *

def get_password_length():
	password_length = input("\nHow many characters should your new password be? ")
	try:
		password_length_int = int(password_length)
	except ValueError:
		quit()

	generate_password(password_length_int)


def generate_password(password_length):

	letters = ["a", "b", "c", "d", "e", "f", 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	special_chars = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", ";", ":", "<", "|", ">", "?", "/"]


	password = []


	for number in range(password_length):
		random_letter = letters[random.randint(0, 25)]
		random_number = numbers[random.randint(0, 9)]
		random_special_character = special_chars[random.randint(0, 23)]

		key = random.randint(0, 2)

		if key == 0:
			password.append(random_letter)
		elif key == 1:
			password.append(random_number)
		elif key == 2:
			password.append(random_special_character)

	generated_pswd_lbl = Label(root, text=password).pack()

root = Tk()
root.title("Password Generator")

get_password_length()

root.mainloop()
