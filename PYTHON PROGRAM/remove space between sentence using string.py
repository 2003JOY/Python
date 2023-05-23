#Write a program to remove extra spaces between the words in a string

def removeSpaces(string):
	string = string.replace(' ','')
	return string
	
# Driver program
string = input("Write any Sentence: ")
print(removeSpaces(string))