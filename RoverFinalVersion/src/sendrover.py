from systemrover import Rover
from loadcommands import Command

"""
Load file with input, and start rovers
"""

def main():

	sendCommandsRover = Command.loadInstructions('rovercommands.input')
	
	roverOne = Rover(sendCommandsRover[0])
	roverOne.setRoverCleanLocalization(sendCommandsRover[1].split())
	roverOne.setPositionRover(sendCommandsRover[2])
	
	roverTwo = Rover()
	roverTwo.setRoverCleanLocalization(sendCommandsRover[3].split())
	roverTwo.setPositionRover(sendCommandsRover[4])

if __name__ == '__main__':
	main()
