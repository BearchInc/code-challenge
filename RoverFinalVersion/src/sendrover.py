from systemrover import Rover
from loadcommands import Commands

"""
Load file with input, and start rovers
"""

def main():

	sendCommandsRover = Commands.loadInstructions('rovercommands.input')
	
	roverOne = Rover(sendCommandsRover[0])
	roverOne.getRoverCleanLocalization(sendCommandsRover[1].split())
	roverOne.positionRover(sendCommandsRover[2])
	
	roverTwo = Rover()
	roverTwo.getRoverCleanLocalization(sendCommandsRover[3].split())
	roverTwo.positionRover(sendCommandsRover[4])

if __name__ == '__main__':
	main()
