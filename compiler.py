from Arguments import * # bruh I know, not good practice, don't care, I am using python

class Compiler:
	def __init__(self) -> None:
		self.flags = ArgFlags(0)
		# Trust me, repition makes it easier
		self.options = {
			'-x': con_exe, 
			'-exe': con_exe
			}

	def run(self, args: list[str]):
		for i in range(1, len(args)):
			# Cases for options
			if args[i].startswith('-'):
				option = self.options.get(args[i])
				if option is None:
					# One of two things:
					# To exit and display an error
					# Just skip it and display a warning
					# For now I will exit and display an error
					print(f'the option {args[i]} does not exist')
					return
				i += 1
				option.execute(args[i:i+option.get_arg_count()])
				# I think I should minus by one since the for loop will add by one 
				# but the loop doesn't, idk y??? ('_')
				i += option.get_arg_count()
				if option.get_error_message() is not None:
					print(option.get_error_message())
				