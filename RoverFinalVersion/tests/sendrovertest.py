from systemrovertest import Rover
from loadcommandstest import FileLoad
import unittest

def main():

	commandsRover = FileLoad.loadFile('rovercommands.input')
	
	roverOne = Rover(commandsRover[0])
	roverOne.getRoverCleanLocalization(commandsRover[1].split())
	roverOne.positionRover(commandsRover[2])
	
	roverTwo = Rover()
	roverTwo.getRoverCleanLocalization(commandsRover[3].split())
	roverTwo.positionRover(commandsRover[4])

class MainTest(unittest.TestCase):

	def testMain(self):
		commandsRover = FileLoad.loadFile('rovercommands.input')

		roverOne = Rover(commandsRover[0])
		roverOne.getRoverCleanLocalization(commandsRover[1].split())
		roverOne.positionRover(commandsRover[2])

		self.assertEqual('5 5', commandsRover[0])
		self.assertEqual('1 2 N'.split(), commandsRover[1].split())
		self.assertEqual('LMLMLMLMM', commandsRover[2])

		roverTwo = Rover()
		roverTwo.getRoverCleanLocalization(commandsRover[3].split())
		roverTwo.positionRover(commandsRover[4])

		self.assertEqual('3 3 E'.split(), commandsRover[3].split())
		self.assertEqual('MMRMMRMRRM', commandsRover[4])


if __name__ == '__main__':
	unittest.main()