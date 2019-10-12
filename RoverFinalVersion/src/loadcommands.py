"""
This class load files with commands and split
"""

class Commands:

	@classmethod	
	def loadInstructions(self, nameFile):

		with open(nameFile) as command:
			arrayForCommands =[]
			for line in command:
				arrayForCommands.append(line.rstrip('\n').rstrip())
			return(arrayForCommands)