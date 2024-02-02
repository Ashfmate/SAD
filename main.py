import sys
from lexical_analyser import tokenize, Token

def readToString():
	try:
		with open('file.sad', 'r') as file:
			return file.read()
	except IndexError:
		print("Please provide a file to read", file=sys.stderr)
		exit(1)
	except FileNotFoundError:
		print("The file does not exist, please provide a correct path", file=sys.stderr)
		exit(2)

def main():
	tokens = tokenize(readToString())
	for token in tokens:
		print(token)

if __name__ == '__main__':
	main()