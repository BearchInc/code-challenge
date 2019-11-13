class Command:
	"""
	Load file with commands and split.
	"""

	@classmethod	
	def loadInstructions(self, nameFile):
		"""
		Extended method from class Command, directly load.
		"""

		with open(nameFile) as command:
			arrayForCommands =[]
			for line in command:
				arrayForCommands.append(line.rstrip('\n').rstrip())
			return(arrayForCommands)