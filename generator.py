#Import packages
import time
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic
from os import *

#TODO get the password to generate correctly with all three options


class gui(QMainWindow):
	def __init__(self):
		super(gui, self).__init__()
		uic.loadUi("interface.ui", self)
		self.show()

		self.actionClose.triggered.connect(exit)
		self.generate_pwsd_button.clicked.connect(self.generate_password)

	def generate_password(self):
		pswd_length = int(self.pswd_length_field.text())

		letters = ["a", "b", "c", "d", "e", "f", 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
		spec_chars = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", ";", ":", "<", "|", ">", "?", "/"]

		password = []

		for number in range(pswd_length):

			key = random.randint(0, 2)

			if self.incl_spec_chars_cbox.isChecked() == True:
				password.append(spec_chars[random.randint(0, 23)])
			if self.incl_nums_cbox.isChecked() == True:
				password.append(numbers[random.randint(0, 9)])
			if self.incl_lets_cbox.isChecked() == True:
				password.append(letters[random.randint(0, 50)])



		password_string = ""

		for character in password:
			password_string += str(character)

		self.new_pswd_field.setText(password_string[:pswd_length])



def main():
	app = QApplication([])
	window = gui()
	app.exec_()

if __name__ == '__main__':
	main()


#def generate_password(password_length):
#	password_length_int = int(password_length)
#
#	letters = ["a", "b", "c", "d", "e", "f", 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#	special_chars = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", ";", ":", "<", "|", ">", "?", "/"]
#
#
#	password = []
#
#	for number in range(password_length_int):
#		random_letter = letters[random.randint(0, 25)]
#		random_number = numbers[random.randint(0, 9)]
#		random_special_character = special_chars[random.randint(0, 23)]
##		key = random.randint(0, 2)

#		if key == 0:
#			password.append(random_letter)
#		elif key == 1:
#			password.append(random_number)
#		elif key == 2:
#			password.append(random_special_character)
