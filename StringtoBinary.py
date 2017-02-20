# String to Binary
# Assignment 2
# Brandon Knieriem
# Files: StringtoBinary.py, stb_fx.py
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
# Extra:
# 	- Program with multiple files.
#IMPORTS#########################################################

import stb_fx # Contains basic functions.

#MAIN############################################################
# Loops until user terminates the program via command.
# Takes string of text and converts it, char by char, to binary.
# Each 8 bit set adds 4 CRC bits.
print("\tAssignment 3: String to Binary")
while True :
	text = []
	binary = []

	text = stb_fx.input_text()
	for i in text :
		binary.append(stb_fx.value_to_binary(i))
	stb_fx.print_list(binary)