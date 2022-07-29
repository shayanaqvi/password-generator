import time
import random
import tkinter.ttk
import tkinter.font as font
from ttkthemes import ThemedTk
from tkinter import *
from os import *


def get_password_length():

	sf_mono = font.Font(family='SF Mono')

	global window_frame
	#Frame around the window's contents
	window_frame = ttk.LabelFrame(root)
	window_frame.grid(row=10, column=0, padx=5, pady=5)

	#Your new password is:
	your_password_is_lbl = ttk.Label(window_frame, text="Your new password is: ", font=('SF Mono', 14)).grid(row=0, column=1)

	#Text field that displays the new password
	generated_pwsd_lbl = ttk.Entry(window_frame, width=50, font=('SF Mono', 10), state=DISABLED).grid(row=1, column=1)

	#Enter the length of the password here
	password_length_entry = ttk.Entry(window_frame, width=50, font=('SF Mono', 10))
	password_length_entry.insert(0, "Password length")
	password_length_entry.grid(row=2, column=1)

	#Button to generate password
	button = ttk.Button(window_frame, text="Generate", command=lambda: generate_password(password_length_entry.get()))
	button.grid(row=3, column=1)
#TODO Get theming done with

def generate_password(password_length):
	password_length_int = int(password_length)

	letters = ["a", "b", "c", "d", "e", "f", 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	special_chars = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", ";", ":", "<", "|", ">", "?", "/"]


	password = []

	for number in range(password_length_int):
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


	generated_pswd_lbl = Entry(window_frame, width=50)
	generated_pswd_lbl.insert(0, password)
	generated_pswd_lbl.grid(row=1, column=1)

root = ThemedTk(theme="adapta")
root.config(bg='white')
root.title("Password Generator")




get_password_length()

root.mainloop()
