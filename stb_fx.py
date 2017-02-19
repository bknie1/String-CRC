#IMPORTS#########################################################

import sys # For 'quit'.
import crc # Contains specific error checking functions.

#FUNCTIONS#######################################################
def input_text() :
	text = input("Enter a single character, string, or 'quit': ")
	if(text == 'quit') : sys.exit()
	if(len(text) < 1) :
		print("Error: Invalid entry.")
		input_char()
	return text
#----------------------------------------------------------------
# 33-44: Non-library fx binary conversion.
# 35: ord() function returns index in ASCII code.
# 45-46: Calls and adds the 4-bit CRC function before returning
# the complete sequence to our "main" procedure.
def value_to_binary (value) :
	print("Value to Binary")
	binary = ""
	value = ord(value)

	i = 0 # DEBUG

	while value != 0 :
		print("Value:", value)
		print(i) # DEBUG
		i += 1 # DEBUG
		if value % 2 == 0 :
			binary = "0" + binary
		else :
			binary = "1" + binary
		value //= 2
	print_list(binary)
	binary = add_error_checking(binary)
	return binary
#----------------------------------------------------------------
# Evaluates and adds CRC bits.
def add_error_checking(binary) :
	print("Add Error Bits")
	binary = crc.check_c1(binary)
	binary = crc.check_c2(binary)
	binary = crc.check_c4(binary)
	binary = crc.check_c8(binary)
	return binary
#----------------------------------------------------------------
def print_list(text) :
	print("Length:", len(text))
	for i in text :
		print(i, end="")
	print("\n")
#----------------------------------------------------------------