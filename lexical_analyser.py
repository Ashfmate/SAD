from enum import Enum, auto
import re


class Token(Enum):
	IDENT = (auto(), str)
	FULL_COLON = auto()
	OPERATOR = (auto(), str)
	DATA_TYPE = (auto(), str)
	LEFT_PAREN = auto()
	RIGHT_PAREN = auto()
	WHITESPACE = auto()


class Pattern:
	def __init__(self, pat: str, token: Token) -> None:
		self.pat = pat
		self.token = token

	def __str__(self) -> str:
		return self.token.name

patterns = [
		Pattern(r'int|char|float', Token.DATA_TYPE),
		Pattern(r'[a-zA-Z]\w*', Token.IDENT),
		Pattern(r':', Token.FULL_COLON),
		Pattern(r'\(', Token.LEFT_PAREN),
		Pattern(r'\)', Token.RIGHT_PAREN),
		Pattern(r'\+\+|/|\*|\+|-|&&|\|\||&|\||=', Token.OPERATOR),
		Pattern(r'\s+', Token.WHITESPACE)
	]
lexeme_pats = [Token.DATA_TYPE, Token.OPERATOR, Token.IDENT]

def get_match(pat: Pattern, code: str) -> (str, Token):
	if match:= re.match(pat.pat, code):
		return (match.group(), pat.token)
	return None

def tokenize(code: str):
	index = 0
	size = len(code)
	tokens = []
	while index < size:
		token = list(filter(lambda item: item,map(lambda item: get_match(item, code[index:]), patterns)))
		if len(token) == 0:
			index += 1
			continue
		(lexeme,token) = token[0]
		index += len(lexeme)
		if token is Token.WHITESPACE:
			continue
		if token in lexeme_pats:
			token = (str(token), lexeme)
		tokens.append(token)
	return tokens
