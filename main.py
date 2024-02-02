import sys
from lexical_analyser import tokenize
import pandas as pd

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
	table = {
		'Token Name': [],
		'Lexeme': []
	}
	for token in tokens:
		table['Token Name'].append(token[0].name)
		table['Lexeme'].append(token[1])

	print(pd.DataFrame(table))

if __name__ == '__main__':
	main()