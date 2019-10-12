from systemrovertest import Rover
from loadcommandstest import Commands
import unittest

def main():

	sendsendCommandsRover = Commands.loadInstructions('rovercommands.input')
	
	roverOne = Rover(sendCommandsRover[0])
	roverOne.getRoverCleanLocalization(sendCommandsRover[1].split())
	roverOne.positionRover(sendCommandsRover[2])
	
	roverTwo = Rover()
	roverTwo.getRoverCleanLocalization(sendCommandsRover[3].split())
	roverTwo.positionRover(sendCommandsRover[4])

class MainTest(unittest.TestCase):

	def testMain(self):
		sendCommandsRover = Commands.loadInstructions('rovercommands.input')
		self.assertEqual(['5 5', '1 2 N', 'LMLMLMLMM', '3 3 E', 'MMRMMRMRRM'], sendCommandsRover)

		roverOne = Rover(sendCommandsRover[0])
		roverOne.getRoverCleanLocalization(sendCommandsRover[1].split())
		roverOne.positionRover(sendCommandsRover[2])

		self.assertEqual('5 5', sendCommandsRover[0])
		self.assertEqual('1 2 N'.split(), sendCommandsRover[1].split())
		self.assertEqual('LMLMLMLMM', sendCommandsRover[2])

		roverTwo = Rover()
		roverTwo.getRoverCleanLocalization(sendCommandsRover[3].split())
		roverTwo.positionRover(sendCommandsRover[4])

		self.assertEqual('3 3 E'.split(), sendCommandsRover[3].split())
		self.assertEqual('MMRMMRMRRM', sendCommandsRover[4])


if __name__ == '__main__':
	unittest.main()