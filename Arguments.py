from enum import Enum

class ArgFlags(Enum):
	NoFlag = 0
	FileFound = 1
	WarnAll = 2
	WarnExtra = 4
	WarnToError = 8
	Debugging = 16

class Option:
	def __init__(self, function, arg_count: int, description: str, error_messages: list[str]):
		self.function = function
		self.arg_count = arg_count
		self.description = description
		self.error_messages = error_messages
		self.error_number = None
	
	def get_error_message(self):
		if self.error_number is None:
			return None
		else:
			return self.error_messages[self.error_number]
		
	def get_arg_count(self):
		return self.arg_count
	
	def get_description(self):
		return self.description
	
	def execute(self, args: list[str]):
		self.error_number = self.function(args)
		
# Please end my suffering, I am using a stupid language like python
# Why can't I pass a lambda as an argument, I can only give a one line lambda, who designed this language?

###############################################################################################################################
### Start - File Argument

def file_arg_fn(args: list[str]):
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
		

file_arg = Option(
	file_arg_fn,
	0,
	'Opens a file, and reads it', 
	["Please provide a .sad file", "Please provide a file"]
	)

### End - File Argument
###############################################################################################################################


###############################################################################################################################
### Start - Console Execution

def con_exe_fn(args: list[str]):
	try:
		print(args[0])
	except IndexError:
		return 0
	return None

con_exe = Option(
	con_exe_fn,
	1,
	'Executes the immediate argument as code', 
	['No code provided after the execute option']
	)

### End - Console Execution
###############################################################################################################################