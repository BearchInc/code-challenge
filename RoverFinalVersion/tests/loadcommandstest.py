from systemrovertest import Rover

import unittest

class Commands:

	@classmethod	
	def loadInstructions(self, nameFile):

		with open(nameFile) as command:
			arrayForCommands =[]
			for line in command:
				arrayForCommands.append(line.rstrip('\n').rstrip())
			return(arrayForCommands)

class CommandsTest(unittest.TestCase):

	def testloadInstructions(self):
		commandsRover = Commands.loadInstructions('rovercommands.input')
		self.assertEqual(['5 5', '1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM'], commandsRover)


if __name__ == '__main__':
	unittest.main()