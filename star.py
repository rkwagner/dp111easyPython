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
	else:
		a = [ i for i in input[ pos + 2 : ] ]
		c = ''.join( a )
	else:
		a = [ i for i in input[ : pos - 1 ] ]
		b = [ i for i in input[ pos + 2 : ] ]
		c = ''.join( a ) + ''.join( b )

	return stardelete(c)

while True:
	in_string = str( raw_input( "(quit exits)>" ) )
	if in_string != "quit":
		print stardelete(in_string)
	else:
		print "Exit sequence."
		break
