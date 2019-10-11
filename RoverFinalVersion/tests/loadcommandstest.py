from systemrovertest import Rover

import unittest

class FileLoad:

	@classmethod	
	def loadFile(self, nameFile):

		with open(nameFile) as command:
			arrayForCommands =[]
			for line in command:
				arrayForCommands.append(line.rstrip('\n').rstrip())
			return(arrayForCommands)

class FileLoadTest(unittest.TestCase):

	def testLoadFile(self):
		commandsRover = FileLoad.loadFile('rovercommands.input')


if __name__ == '__main__':
	unittest.main()