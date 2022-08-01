# Password generator
A GUI utility that generates a passwords. It does not store any previously generated passwords.
Written in Python and Qt.

## Usage
1. Download this repository
2. Extract its contents
3. Open the extracted folder in the terminal
4. Give the shell script (the file ending in .sh) execution rights ```chmod u+x generate_password.sh```
5. Run the script ```./generate_password.sh```

## Using the script from anywhere
You could create an alias:
1. Edit your .bashrc file, usually located in your ~/ directory
2. Create an alias with your preferred name ```alias generate_password="cd /path/to/executable; ./generate_password; cd -"```
3. Run ```source /path/to/.bashrc```
