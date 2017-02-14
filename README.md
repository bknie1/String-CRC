#Assignment 2
## Python

In the first assignment you wrote a program that would check a received sequence of twelve ones and zeros to determine whether any bits had been corrupted during a transmission. In this program you are going to generate a bit sequence based on an input message. Your program should again have a query loop that allows the user to generate more than one bit sequence. Each time through the loop you should ask the user to input a character message which is read into a string. You should then process this string as follows:

1) Write a function that takes a single character as input and returns a list containing eight ones and zeros that represents the binary form of the character's value in the ASCII sequence. You can determine a character's index in the ASCII code using the ord() function. You should convert this index value into its binary equivalent using the repeated division by 2 method we used in our class program, except this time you should generate a list of integer 1 and 0 values rather than a string.

2) Write a function that takes a list containing eight ones and zeros and returns a new list containing the 12 bits corresponding to the error correction code used in the first assignment. This time, when you examine the appropriate subset of data bits, you will not be looking to see if a check bit is correct. You will be calculating the correct check bit value that goes with the even or odd number of ones in the data bits. Once you have generated these four check bits, you can create the list of 12 bit values that will be sent in a transmission for that data byte. Return this list.

3) Using these two functions, create a single list of ones and zeros that corresponds to the data transmission you would make for your input message, having converted each character into its corresponding 12 bits. Then print out this data transmission sequence.

Properly document your program. Submit your source file, as well as sample output of your program in action. Once again, only use aspects of the language we have talked about so far, or I have mentioned here.
