import re
import sys


def read_to_string() -> str | None:
    """
    Read the content of a file specified in the command line arguments and return it as a string.

    Returns:
    str: The content of the file as a string.
    """
    try:
        file_path: str = sys.argv[1]
        with open(file_path, 'r') as file:
            return file.read()
    except IndexError:
        print("Please provide a file to read",
              file=sys.stderr)
        exit(1)
    except FileNotFoundError:
        print("The file does not exist, please provide a correct path",
              file=sys.stderr)
        exit(2)


def tokenize(code: str, patterns: list[(str, str)]) -> list:
    tokens = []
    index = 0
    while index < len(code):
        found = False
        for pat, token in patterns:
            if match := re.match(pat, code[index:]):
                index += len(match.group())
                if token in ['id', 'data']:
                    token = (token, match.group())
                tokens.append(token)
                found = True
                break
        if not found:
            index += 1
    return tokens


def main():
    patterns: list = [
        (r'int|char|float', 'data'),
        (r'[a-zA-Z]\w*', 'id'),
        (r':', 'data identifier'),
        (r'\(', 'left parenthese'),
        (r'\)', 'right parenthese'),
        (r'\+\+', 'increment operator'),
        (r'/', 'division operator'),
        (r'\*', 'multiplication operator'),
        (r'\+', 'addition operator'),
        (r'-', 'minus operator'),
        (r'&&', 'logical and operator'),
        (r'\|\|', 'logical or operator'),
        (r'&', 'bitwise and operator'),
        (r'\|', 'bitwise or operator'),
        (r'=', 'assignment operator'),
    ]
    tokens: list = tokenize(read_to_string(), patterns)
    for token in tokens:
        print(token)


if __name__ == '__main__':
    main()
