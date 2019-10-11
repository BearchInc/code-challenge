"""
This class load files with commands and split
"""

class FileLoad:

	@classmethod	
	def loadFile(self, nameFile):

		with open(nameFile) as command:
			arrayForCommands =[]
			for line in command:
				arrayForCommands.append(line.rstrip('\n').rstrip())
			return(arrayForCommands)