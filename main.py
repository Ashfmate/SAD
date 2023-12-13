import sys
from compiler import Compiler
# from enum import Enum

def main():
	# file_arg is a variable that will hold the compiling a file
	# It should be noted that it is just an example, it will be changed by a lot
	# This right here is assuming that the first argument passed will be the file argument
	# If the file is not provided at all, "Please provide a file" message will appear
	# If the file is provided but is not a .sad file, "Please provide a .sad file" message will appear
	# If the file is provided and it is a .sad file, for now it will just print the file contents
	com = Compiler()
	com.run(sys.argv)

if __name__ == "__main__":
	main()

# Things to Add
# Add argument parser
# Add more arguments and execute based on the identifiers

# Structure of the team
# +-------------+---------------------------+
# |	Team Number	|			Work			|
# +-------------+---------------------------+
# |		 1		|		  grammar			|
# |		 2		|	creating the compiler	|
# |		 1		|		 arguments			|
# |		 1		|	 language features		|
# +-------------+---------------------------+