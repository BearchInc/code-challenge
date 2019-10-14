from spaceshiptest import SpaceShip
import unittest

class Rover(SpaceShip):

	def __init__(self, sizePlateauX = 5, sizePlateauY = 5):
		pass

	@classmethod
	def setRoverCleanLocalization(self, roverCommand):
		self.__directions = ['N', 'E', 'S', 'W']
		self.positionRoverX = int(roverCommand[0])
		self.positionRoverY = int(roverCommand[1])
		self.__initialDirection = self.__directions.index(roverCommand[2])

	def initialHeading(self):
		return self.__initialDirection
	
	def setPositionRover(self, commands):
		for command in commands:
			if command == 'R':
				self._rightRotateRover()
			elif command == 'L':
				self._leftRotateRover()
			elif command == 'M':
				self.__moveRover()

		return self.getHeadingRover()

	def __moveRover(self):
		if(self.__checkNorth()): # North
			self.positionRoverY += 1

		if(self.__checkSouth()): # South
			self.positionRoverY -= 1

		if(self.__checkEast()): # East
			self.positionRoverX += 1

		if(self.__checkWeast()): # Weast
			self.positionRoverX -= 1

		return True

	def __checkNorth(self):
		return self.initialHeading() == 0

	def __checkSouth(self):
		return self.initialHeading() == 2

	def __checkEast(self):
		return self.initialHeading() == 1

	def __checkWeast(self):
		return self.initialHeading() == 3

	def _rightRotateRover(self):
		self.__initialDirection = 0 if self.initialHeading() == 3 else self.initialHeading() + 1
		return self.__initialDirection

	def _leftRotateRover(self):
		self.__initialDirection = 3 if self.initialHeading() == 0 else self.initialHeading() - 1
		return self.__initialDirection

	def getHeadingRover(self):
		return f'{self.positionRoverX} {self.positionRoverY} {self.__directions[int(self.initialHeading())]}'

class RoverTest(unittest.TestCase):

	def testMoveRover(self):
		rover = Rover(5, 5)
		rover.setRoverCleanLocalization([1, 2, 'N'])
		self.assertEqual('1 3 N', rover.setPositionRover('LMLMLMLMM'))

	def testRoverPosition(self):
		rover = Rover(5, 5)
		rover.setRoverCleanLocalization([1, 2, 'N'])

		self.assertEqual(0, rover.initialHeading())
		self.assertEqual(3, rover._leftRotateRover())
		self.assertEqual(0, rover._rightRotateRover())
		self.assertEqual(1, rover._rightRotateRover())
		self.assertEqual(2, rover._rightRotateRover())

	def testMoveRoverFront(self):
		rover = Rover(5, 5)
		rover.setRoverCleanLocalization([1, 2, 'N'])

	def testLocationPositionNorth(self):
		rover = Rover(5, 5)
		rover.setRoverCleanLocalization([1, 2, 'N'])
		rover.setPositionRover("LMLMLMLMM")

		self.assertEqual(1, rover.positionRoverX)
		self.assertEqual(3, rover.positionRoverY)

	def testLocationPositionSouth(self):
		rover = Rover(5, 5)
		rover.setRoverCleanLocalization([1, 2, 'S'])
		rover.setPositionRover("MMMMM")

		self.assertEqual(1, rover.positionRoverX)
		self.assertEqual(-3, rover.positionRoverY)

	def testLocationPositionEast(self):
		rover = Rover(5, 5)
		rover.setRoverCleanLocalization([1, 2, 'E'])
		rover.setPositionRover("MMMM")

		self.assertEqual(5, rover.positionRoverX)
		self.assertEqual(2, rover.positionRoverY)

	def testLocationPositionOest(self):
		rover = Rover(5, 5)
		rover.setRoverCleanLocalization([1, 2, 'W'])
		rover.setPositionRover("MMMMMM")
		
		self.assertEqual(-5, rover.positionRoverX)
		self.assertEqual(2, rover.positionRoverY)

if __name__ == '__main__':
	unittest.main()