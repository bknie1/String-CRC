# String to Binary
# Assignment 2
# Brandon Knieriem
# Goals:
# 	- Generate bit sequence based on input.
# 	- Query loop to generate 1+ bit sequence.
# 	- Process input as string.
# 	- fx1: Takes single char. Returns binary.
# 		- ord() function returns index in ASCII code.
# 		- Generate a list of 1's, 0's.
# 	- fx2: Takes bin list. Returns error correction 12-bit list.
# 		- Calculate the correct bits.
# 	- Create a single binary list comprised of each 12-bit sequence.
# 	- fx3: Print.
#IMPORTS#########################################################

import sys

#FUNCTIONS#######################################################
def input_text() :
	text = input("Enter a single character, string, or 'quit': ")
	if(text == 'quit') : sys.exit()
	if(len(text) < 1) :
		print("Error: Invalid entry.")
		input_char()
	return text
#----------------------------------------------------------------
# From lecture. Simple single value mod 2 conversion.
# 35: ord() function returns index in ASCII code.
def value_to_binary (value) :
	if value == "" :
		binary = "0"
	else :
		binary = ""
		value = ord(value)

		while value != 0 :
			if value % 2 == 0 :
				binary = "0" + binary
			else :
				binary = "1" + binary
			value //= 2

	return binary
#----------------------------------------------------------------
def print_list(text) :
	for i in text :
		print(i, end="")
	print("\n")
#----------------------------------------------------------------
#MAIN############################################################
# Loops until user terminates the program via command.
# Takes string of text and converts it, char by char, to binary.
# Each 8 bit set adds 4 CRC bits.
print("\tAssignment 3: String to Binary")
while True :
	text = []
	binary = []

	text = input_text()

	for i in text :
		binary.append(value_to_binary(i))

	print_list(binary)