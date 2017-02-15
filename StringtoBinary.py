# String to Binary
# Assignment 2
# Brandon Knieriem
# Goals:
# 	Write the program.
#IMPORTS#########################################################

import sys

#FUNCTIONS#######################################################
def input_char() :
	value = input("Enter a single character, string, or 'quit': ")
	if(value == 'quit') : sys.exit()
	if(len(value) != 1) :
		print("Error: Invalid entry.")
		input_char()
	return value
#----------------------------------------------------------------
def to_binary(value) :
	int_part = ord(value) # Find ASCII code index.
	bin_int = []
	# Convert to Binary
	while int_part != 0 :
		if int_part % 2 == 0 : # If there is no remainder...
			bin_int.append(0) # Binary 0.
		else : # If there is a remainder... there can only be '1'.
			bin_int.append(1)
		int_part //= 2
	print("Binary value of", value, ":", end=' ')
	for i in bin_int :
		print(bin_int[i], end="")
	print("")
#----------------------------------------------------------------
#
#MAIN############################################################
print("\tAssignment 3: String to Binary")
while True :
	value = input_char()
	to_binary(value)
