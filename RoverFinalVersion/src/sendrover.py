from systemrover import Rover
from loadcommands import FileLoad

"""
Load file with input, and start rovers
"""

def main():

	commandsRover = FileLoad.loadFile('rovercommands.input')
	
	roverOne = Rover(commandsRover[0])
	roverOne.getRoverCleanLocalization(commandsRover[1].split())
	roverOne.positionRover(commandsRover[2])
	
	roverTwo = Rover()
	roverTwo.getRoverCleanLocalization(commandsRover[3].split())
	roverTwo.positionRover(commandsRover[4])

if __name__ == '__main__':
	main()
