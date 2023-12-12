class Option:
	def __init__(self, identifiers: [str], function , description: str, error_messages: [str]):
		self.identifiers = identifiers
		self.function = function
		self.description = description
		self.error_messages = error_messages
		self.error_number = None
	
	def error_message(self):
		if self.error_number is None:
			return None
		else:
			return self.error_messages[self.error_number]
	
	def get_identifiers(self):
		return self.identifiers
	
	def get_description(self):
		return self.description
	
	def execute(self, args: [str]):
		self.error_number = self.function(args)
		res = Option(self.identifiers, self.function, self.description, self.error_messages)
		res.error_number = self.error_number
		return res
		


###############################################################################################################################
### Start - File Argument

def file_arg_fn(args: [str]):
	# Tries to open a file in read mode
	try:
		with open(args[0], 'r') as file:
			print(file.read())
	# If the file does not exist, return 0 (the error code for no file existing)
	except FileNotFoundError:
		return 0
	except IndexError:
		return 1
	# If the exception is not hit, then we did not encounter an error, so we can return None
	return None
		

file_arg = Option('', file_arg_fn, 'Opens a file, and reads it', ["Please provide a .sad file", "Please provide a file"])

### End - File Argument
###############################################################################################################################