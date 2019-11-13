from systemrover import Rover
from loadcommands import Command

def main():
	"""
	Main function of Rovers when running from command line.
	"""

	sendCommandsRover = Command.loadInstructions('rovercommands.input')
	
	roverOne = Rover(sendCommandsRover[0])
	roverOne.setRoverCleanLocalization(sendCommandsRover[1].split())
	roverOne.setPositionRover(sendCommandsRover[2])
	
	roverTwo = Rover()
	roverTwo.setRoverCleanLocalization(sendCommandsRover[3].split())
	roverTwo.setPositionRover(sendCommandsRover[4])

if __name__ == '__main__':
	main()
