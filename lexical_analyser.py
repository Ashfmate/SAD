from enum import Enum, auto
import re

class Token(Enum):
	IDENT = auto()
	FULL_COLON = auto()
	OPERATOR = auto()
	DATA_TYPE = auto()
	VISIBILITY = auto()
	LEFT_PAREN = auto()
	RIGHT_PAREN = auto()
	WHITESPACE = auto()
	INTEGRAL = auto()
	REAL = auto()

class Pattern:
	def __init__(self, pat: str, token: Token) -> None:
		self.pat = pat
		self.token = token

patterns = [
		Pattern(r'int|char|float', Token.DATA_TYPE),
		Pattern(r'public|private|protected', Token.VISIBILITY),
		Pattern(r'[a-zA-Z]\w*', Token.IDENT),
		Pattern(r'\d+.\d+', Token.REAL),
		Pattern(r'\d+', Token.INTEGRAL),
		Pattern(r':', Token.FULL_COLON),
		Pattern(r'\(', Token.LEFT_PAREN),
		Pattern(r'\)', Token.RIGHT_PAREN),
		Pattern(r'\+\+|/|\*|\+|-|&&|\|\||&|\||=', Token.OPERATOR),
		Pattern(r'\s+', Token.WHITESPACE)
	]

def get_match(pat: Pattern, code: str) -> (str, Token):
	if match:= re.match(pat.pat, code):
		return (match.group(), pat.token)
	return None

def discern_token(tokens: []):
	if len(tokens) == 0:
		return None
	return max(tokens, key=lambda item: len(item[0]))

def tokenize(code: str):
	index = 0
	size = len(code)
	tokens = []
	while index < size:
		token = map(lambda item: get_match(item, code[index:]), patterns)
		token = filter(lambda item: item, token)
		token = discern_token(list(token))
		if token is None:
			index += 1
			continue
		(lexeme,token) = token
		index += len(lexeme)
		if token is Token.WHITESPACE:
			continue
		tokens.append((token, lexeme))
	return tokens
