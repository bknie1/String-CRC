# Error Checking Bits
# Notes: Modified from Assignment 1.
# Brandon Knieriem
# Goals:
# 	Add CRC bits to an existing 8-bit binary value.
# Notes:
# 	  Complete (12 bits):
# 	  c1 = 0	c2 = 1		d1 = 2		c4 = 3		d2 = 4
# 	  d3 = 5 	d4 = 6		c8 = 7		d5 = 8		d6 = 9
# 	  d7 = 10	d8 = 11
#IMPORTS########################################################

# None.

#FUNCTIONS######################################################
# Insert 1/0 into specific position based on evaluation.
def insert_bit(binary, check, pos) :
	binary = list(binary)
	if check : # If True/Even, add 0.
		binary.insert(pos, 0)
	else : # If False/Odd, add 1.
		binary.insert(pos, 1)
	print_bin(len(binary), binary) # DEBUG
	return binary
#-----------------------------------------------------------------
# d1, d2, d4, d5, d7. Adding c1/pos. 0
# 	  for check_c1 (8 bits):
# 	  c1 = 		c2 =  		d1 = 0		c4 =  		d2 = 1
# 	  d3 = 2 	d4 = 3		c8 =  		d5 = 4		d6 = 5
# 	  d7 = 6	d8 = 7
def check_c1(binary) :
	print_bin(len(binary), binary) # DEBUG
	eval_digits = [
	binary[0], binary[1], binary[3], binary[4], binary[6]]
	check = evaluate(eval_digits)
	binary = insert_bit(binary, check, 0) # 0 is c1's position.
	return binary
#-----------------------------------------------------------------
# d1, d3, d4, d6, d7. Adding c2/pos. 1
# for check_c2 (9 bits):
# 	  c1 = 0	c2 =  		d1 = 1		c4 =  		d2 = 2
# 	  d3 = 3 	d4 = 4		c8 =  		d5 = 5		d6 = 6
# 	  d7 = 7 	d8 = 8
def check_c2(binary) :
	eval_digits = [
	binary[1], binary[3], binary[4], binary[6], binary[7]]
	check = evaluate(eval_digits)
	binary = insert_bit(binary, check, 1) # 1 is c2's position.
	print_bin(binary) # DEBUG
	return binary
#-----------------------------------------------------------------
# d2, d3, d4, d8. Adding c4/pos 3.
# for check_c4 (10 bits):
# 	  c1 = 0	c2 = 1 		d1 = 2		c4 =  		d2 = 3
# 	  d3 = 4 	d4 = 5		c8 =  		d5 = 6		d6 = 7
# 	  d7 = 8 	d8 = 9
def check_c4(binary) :
	eval_digits = [binary[3], binary[4], binary[5], binary[9] ]
	check = evaluate(eval_digits)
	binary = insert_bit(binary, check, 3) # 0 is c4's position.
	print_bin(binary) # DEBUG
	return binary
#-----------------------------------------------------------------
# d5, d6, d7, d8. Adding c8/pos. 7.
# for check_c8 (11 bits):
# 	  c1 = 0	c2 = 1 		d1 = 2		c4 = 3 		d2 = 4
# 	  d3 = 5 	d4 = 6		c8 =  		d5 = 7		d6 = 8
# 	  d7 = 9 	d8 = 10
def check_c8(binary) :
	eval_digits = [binary[7], binary[8], binary[9], binary[10] ]
	check = evaluate(eval_digits)
	binary = insert_bit(binary, check, 7) # 0 is c8's position.
	print_bin(binary) # DEBUG
	return binary
#-----------------------------------------------------------------
#Odd or even number of '1's? Even = True, Odd = False
def evaluate(eval_digits) :
	total = 0
	for i in eval_digits :
		if(i == '1') : total += 1
	if(total % 2 == 0) :
		return True # Even, CRC bit should be 0
	if(total % 2 == 1) :
		return False # Odd, CRC bit should be 1
#-----------------------------------------------------------------
def print_bin(length, binary) :
	print("Length:", length)
	for i in binary :
		print(i, end="")
	print("\n")