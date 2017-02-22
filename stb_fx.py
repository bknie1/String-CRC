#IMPORTS#########################################################

import sys # For 'quit'.
import crc # Contains specific error checking functions.

#FUNCTIONS#######################################################
def input_text() :
	text = input("Enter text or 'quit': ")
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
# 30: NOTE: This seems odd. Refused to run for a full 8 bits.
def value_to_binary (value) :
	binary = ""
	value = ord(value)

	while value != 0 :
		if value % 2 == 0 :
			binary = "0" + binary
		else :
			binary = "1" + binary
		value //= 2
	 # If the length < 8 bits, add 0's to make up for it.
	if len(binary) < 8 :
		i = 0
		while i <= (8 - len(binary)) :
			binary = "0" + binary
			i += 1

	print("Length:", len(binary))
	binary = add_error_checking(binary)
	return binary
#----------------------------------------------------------------
# Evaluates and adds CRC bits.
def add_error_checking(binary) :
	binary = crc.check_c1(binary)
	binary = crc.check_c2(binary)
	binary = crc.check_c4(binary)
	binary = crc.check_c8(binary)
	return binary
#----------------------------------------------------------------
def print_list(binary) :
	print(' '.join(([''.join([str(e) for e in i]) for i in binary])))
#----------------------------------------------------------------