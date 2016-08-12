'''
Star delete - takes an input string and removes any star, as well as
one character to the left and right of the star.
Author:		Ryan Wagner
Date:		August 26, 2014
Description:	Star Delete - deletes characters before and after any star
		entered into the string.
Input:		Input string, "quit" exits the program.
Output:		Formatted string, with star deletion.
'''

def stardelete(input):
	pos = input.find( "*" )
	if pos == -1:
		return input
	elif pos == 0:
		c = input[pos+2:]
	else:
		c = input[:pos-1] + input[pos+2:]

    #causes a recursive call that continues until no stars are found.
	return stardelete(c)

while True:
	in_string = raw_input( "(quit exits)>" )
	if in_string == "quit":
		print "Program terminated."
		break
	print stardelete(in_string)
