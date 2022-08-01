#Import packages
import time
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic
from os import *

#The window that generates the username and password
class Generate_Login_Information(QMainWindow):
	def __init__(self):

		super(Generate_Login_Information, self).__init__()

		self.setFixedSize(800, 448)

		uic.loadUi("interface.ui", self)
		self.show()

		self.setEnabled(True)
		self.actionClose.triggered.connect(self.close_window)



		self.generate_pwsd_button.clicked.connect(self.generate_password)
		self.generate_uname_button.clicked.connect(self.generate_uname)

	#Close the window
	def close_window(self):
		self.hide()

	#Generate the username
	def generate_uname(self):
		pref_words = ["tiny", "lucky", "far", "unsuitable", "melted", "eager", "dependent", "complex", "puzzling", "impartial", "plant", "able", "materialistic", "based", "pure", "many", "free", "delirious", "cultural", "right", "nifty", "resolute", "pushy", "smooth", "sincere", "comptetitive", "difficult", "tasteful", "various", "symptomatic", "overjoyed", "weak", "truculent", "receptive", "endurable", "mature", "envious", "sudden", "swanky", "absurd", "private", "juicy", "instinctive", "deeply", "adorable", "colourful", "opposite", "gorgeous", "obvious", "accidental", "staking", "guttural", "blushing", "heartbreaking", "sore", "sticky", "far", "detailed", "crabby", "sturdy", "cultural", "jealous", "beneficial", "nimble", "useful", "quack", "unequal", "whispering", "unequaled", "productive", "uncovered", "delicious", "hard", "soft", "pentinent", "juicy", "powerful", "flippant", "nasty", "cold", "guarded", "slippery", "biased", "cuddly", "talented", "fearful", "obviously", "sudden", "next", "shy", "direful", "foolish", "fast", "upset", "tender", "acrid", "civil" ,"consciou", "deep", "solid"]
		suf_words = ["cat", "climate", "theory", "role", "region", "king", "virus", "excitement", "perspective", "pollution", "cabinet", "story", "actor", "consequence", "injury", "newspaper", "language", "hall", "tale", "accident", "assignment", "republic", "length", "signature", "establishment", "manager", "drawing", "grocery", "protection", "dealer", "winner", "storage", "basis", "instance", "potato", "wedding", "message", "introduction", "son", "recording", "appointment", "interaction", "lab", "village", "organization", "chemistry", "enthusiasm", "ad", "celebration", "addition", "cell", "affair", "guest", "county", "shopping", "finding", "news", "science", "history", "poem" "army", "hair", "friend", "republic", "hat", "actor", "health", "sector", "agency", "software", "father", "mother", "coffee", "atmosphere", "breath", "goal", "awareness", "error", "recipe", "blood", "fact", "disaster", "application", "activity", "apartment", "depth", "drink", "control", "collection", "description", "pie", "meal", "instructio", 'surgery', 'volume', 'committee', 'explanatio', 'hotel', 'department', 'departure']
		numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

		frst_word = pref_words[random.randint(0, (len(pref_words) - 1))]
		scnd_word = suf_words[random.randint(0, (len(suf_words) - 1))]
		rand_num_1 = numbers[random.randint(0, (len(numbers) - 1))]
		rand_num_2 = numbers[random.randint(0, (len(numbers) - 1))]


		final_username = ""

		while True:

			if self.incl_uname_nums_cbox.isChecked() == True:
				if self.incl_uname_cpt_cbox.isChecked() == True:
					final_username = f"{frst_word.title()}{scnd_word.title()}{rand_num_1}{rand_num_2}"
					self.new_uname_field.setText(final_username)
					self.final_uname_field.setText(final_username)
					break
				else:
					final_username = f"{frst_word}{scnd_word}{rand_num_1}{rand_num_2}"
					self.new_uname_field.setText(final_username)
					self.final_uname_field.setText(final_username)
					break

			if self.incl_uname_cpt_cbox.isChecked() == True:
				if self.incl_uname_nums_cbox.isChecked() == True:
					final_username = f"{frst_word.title()}{scnd_word.title()}{rand_num_1}{rand_num_2}"
					self.new_uname_field.setText(final_username)
					self.final_uname_field.setText(final_username)
					break
				else:
					final_username = f"{frst_word.title()}{scnd_word.title()}"
					self.new_uname_field.setText(final_username)
					self.final_uname_field.setText(final_username)
					break

			if self.incl_uname_nums_cbox.isChecked() == False or self.incl_uname_cpt_cbox.isChecked() == False:
				final_username = f"{frst_word}{scnd_word}"
				self.new_uname_field.setText(final_username)
				self.final_uname_field.setText(final_username)
				break

	#Generate the password
	def generate_password(self):
		pswd_length = int(self.pswd_length_field.text())

		letters = ["a", "b", "c", "d", "e", "f", 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
		spec_chars = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "=", "+", "[", "]", ";", ":", "<", "|", ">", "?", "/"]

		password = []

		for number in range(pswd_length):

			key = random.randint(0, 2)

			if key == 0:
				if self.incl_spec_chars_cbox.isChecked() == True:
					password.append(spec_chars[random.randint(0, 23)])
				else:
					subkey = random.randint(0, 1)

					if self.incl_nums_cbox.isChecked() == True:
						if subkey == 0:
							password.append(numbers[random.randint(0, 9)])
						if subkey == 1:
							password.append(numbers[random.randint(0, 9)])
					if self.incl_lets_cbox.isChecked() == True:
						if subkey == 0:
							password.append(letters[random.randint(0, 50)])
						if subkey == 1:
							password.append(letters[random.randint(0, 50)])
			elif key == 1:
				if self.incl_nums_cbox.isChecked() == True:
					password.append(numbers[random.randint(0, 9)])
				else:
					subkey = random.randint(0, 1)

					if self.incl_spec_chars_cbox.isChecked() == True:
						if subkey == 0:
							password.append(spec_chars[random.randint(0, 23)])
						if subkey == 1:
							password.append(spec_chars[random.randint(0, 23)])

					if self.incl_lets_cbox.isChecked() == True:
						if subkey == 0:
							password.append(letters[random.randint(0, 50)])
						if subkey == 1:
							password.append(letters[random.randint(0, 50)])


			elif key == 2:
				if self.incl_lets_cbox.isChecked() == True:
					password.append(letters[random.randint(0, 50)])
				else:
					subkey = random.randint(0, 1)

					if self.incl_nums_cbox.isChecked() == True:
						if subkey == 0:
							password.append(numbers[random.randint(0, 9)])
						if subkey == 1:
							password.append(numbers[random.randint(0, 9)])
					if self.incl_spec_chars_cbox.isChecked() == True:
						if subkey == 0:
							password.append(spec_chars[random.randint(0, 23)])
						if subkey == 1:
							password.append(spec_chars[random.randint(0, 23)])



		password_string = ""

		for character in password:
			password_string += str(character)

		self.new_pswd_field.setText(password_string[:pswd_length])
		self.final_pswd_field.setText(password_string[:pswd_length])

#The window that shows saved passwords
class View_Login_Information(QMainWindow):
	def __init__(self):
		super(View_Login_Information, self).__init__()

		self.setFixedSize(800, 448)
		uic.loadUi("view.ui", self)
		self.show()

		self.actionClose.triggered.connect(self.close_window)

	#Close the window
	def close_window(self):
		self.hide()

#The window that gives you the option to create a new login, or view saved logins
class Introduction(QDialog):
	def __init__(self):
		super(Introduction, self).__init__()
		uic.loadUi("option.ui", self)
		self.show()

		self.crt_login.clicked.connect(lambda: self.show_new_window(Generate_Login_Information()))
		self.vw_login.clicked.connect(lambda: self.show_new_window(View_Login_Information()))
		self.quit.clicked.connect(exit)


	#Display a new window based on the button
	def show_new_window(self, window_name):
		self.new_window = window_name
		self.new_window.show()



#Run the app
def main():
	app = QApplication([])
	window = Introduction()
	app.exec_()

if __name__ == '__main__':
	main()

