import re, sys

def readToString():
	try:
		file = sys.argv[1]
		file = open(file).read()
	except IndexError:
		print("Please provide a file to read", file=sys.stderr)
		exit(1)
	except FileNotFoundError:
		print("The file does not exist, please provide a correct path", file=sys.stderr)
		exit(2)
	return file

def tokenize(code: str, patterns: list[(str, str)]):
	index = 0
	tokens = []
	while index < len(code):
		found = False
		for (pat, token) in patterns:
			match = re.match(pat, code[index:])
			if match:
				found = True
				index += len(match.group())
				if token in ['id','data', 'operator']:
					token = f'{token} : {match.group()}'
				tokens.append(token)
				break
		if not found:
			index += 1
	return tokens


def main():
	patterns = [
		(r'int|char|float', 'data'),
		(r'[a-zA-Z]\w*', 'id'),
		(r':','data identifier'),
		(r'\(', 'left parenthese'),
		(r'\)', 'right parenthese'),
		(r'++|/|\*|\+|-|&&|\|\||&|\||=', 'operator'),
	]
	tokens = tokenize(readToString(), patterns)
	for token in tokens:
		print(token)

if __name__ == '__main__':
	main()