from spaceshiptest import SpaceShip
import unittest

directions = ['N', 'E', 'S', 'W']

class Rover(SpaceShip):
	pass

	def __init__(self):
		self.positionRoverX = 0
		self.positionRoverY = 0
		#0 North, 1 east, 2 south, 3 weast
		self.initialDirection = directions.index('N')

		#(1, 2, 0)
		#(1, 2, N)
		#LMLMLMLMM
		#(1, 3, N)

	def positionRover(self, commands=''):
		for command in commands:
			if command == 'R':
				self.rightRotateRover()
			elif command == 'L':
				self.leftRotateRover()
			elif command == 'M':
				self.moveRover()

		directions = ['N', 'E', 'S', 'W'][self.initialDirection]
		return f'{self.positionRoverX} {self.positionRoverY} {directions}'
		print(f'{self.positionRoverX} {self.positionRoverY} {directions}')

	def moveRover(self):

		if(self.initialDirection == 0): # North
			self.positionRoverY +=1

		if(self.initialDirection == 2): # South
			self.positionRoverY -= 1

		if(self.initialDirection == 1): # East
			self.positionRoverX += 1

		if(self.initialDirection == 3): # Weast
			self.positionRoverX -= 1

		return True

	def rightRotateRover(self):
		self.initialDirection = 0 if self.initialDirection == 3 else self.initialDirection + 1
		return self.initialDirection

	def leftRotateRover(self):
		self.initialDirection = 3 if self.initialDirection == 0 else self.initialDirection - 1
		return self.initialDirection

class RoverTest(unittest.TestCase):

	def testMove(self):
		roverSubOne = Rover()
		self.assertEqual('0 1 N', roverSubOne.positionRover("LMLMLMLMM"))

		roverSubTwo = Rover()
		self.assertEqual('2 2 N', roverSubTwo.positionRover("MMRMMRMRRM"))

	#def testInitialPosition(self):
	#	rover = Rover(1, 2, 'E')
	#	self.assertEqual('5 5', rover.plateauPosition(int(x), int(y)))


	def testRoverPosition(self):
		roverOne = Rover()
		self.assertEqual(0, roverOne.initialDirection)
		print('North = 0')
		self.assertEqual(3, roverOne.leftRotateRover())
		print('Weast = 3')
		self.assertEqual(0, roverOne.rightRotateRover())
		print('North = 0')
		self.assertEqual(1, roverOne.rightRotateRover())
		print('East = 1')
		self.assertEqual(2, roverOne.rightRotateRover())
		print('South = 2')

	def testMoveRorverFront(self):
		roverOne = Rover()
		self.assertEqual(1, roverOne.moveRover())

	def testLocationPositionNorth(self):
		roverOne = Rover()
		roverOne.positionRover("LMLMLMLMM")

		roverOne.moveRover()
		self.assertEqual(0, roverOne.positionRoverX)
		self.assertEqual(2, roverOne.positionRoverY)

		roverOne.moveRover()
		self.assertEqual(0, roverOne.positionRoverX)
		self.assertEqual(3, roverOne.positionRoverY)

		roverOne.moveRover()
		self.assertEqual(0, roverOne.positionRoverX)
		self.assertEqual(4, roverOne.positionRoverY)

		roverOne.moveRover()
		self.assertEqual(0, roverOne.positionRoverX)
		self.assertEqual(5, roverOne.positionRoverY)

		roverOne.moveRover()
		self.assertEqual(0, roverOne.positionRoverX)
		self.assertEqual(6, roverOne.positionRoverY)

	def testLocationPositionSouth(self):
		rovertTwo = Rover()
		rovertTwo.positionRover("RRMM")

		rovertTwo.moveRover()
		self.assertEqual(0, rovertTwo.positionRoverX)
		self.assertEqual(-3, rovertTwo.positionRoverY)

		rovertTwo.moveRover()
		self.assertEqual(0, rovertTwo.positionRoverX)
		self.assertEqual(-4, rovertTwo.positionRoverY)

		rovertTwo.moveRover()
		self.assertEqual(0, rovertTwo.positionRoverX)
		self.assertEqual(-5, rovertTwo.positionRoverY)

		rovertTwo.moveRover()
		self.assertEqual(0, rovertTwo.positionRoverX)
		self.assertEqual(-6, rovertTwo.positionRoverY)

		rovertTwo.moveRover()
		self.assertEqual(0, rovertTwo.positionRoverX)
		self.assertEqual(-7, rovertTwo.positionRoverY)

	def testLocationPositionEast(self):
		roverThree = Rover()
		roverThree.positionRover("MMRMMRMRRM")

		roverThree.moveRover()
		self.assertEqual(2, roverThree.positionRoverX)
		self.assertEqual(3, roverThree.positionRoverY)

		roverThree.moveRover()
		self.assertEqual(2, roverThree.positionRoverX)
		self.assertEqual(4, roverThree.positionRoverY)

		roverThree.moveRover()
		self.assertEqual(2, roverThree.positionRoverX)
		self.assertEqual(5, roverThree.positionRoverY)

		roverThree.moveRover()
		self.assertEqual(2, roverThree.positionRoverX)
		self.assertEqual(6, roverThree.positionRoverY)

		roverThree.moveRover()
		self.assertEqual(2, roverThree.positionRoverX)
		self.assertEqual(7, roverThree.positionRoverY)

	def testLocationPositionOest(self):
		roverFour = Rover()
		roverFour.positionRover('LMMM')

		roverFour.moveRover()
		self.assertEqual(-4, roverFour.positionRoverX)
		self.assertEqual(0, roverFour.positionRoverY)

		roverFour.moveRover()
		self.assertEqual(-5, roverFour.positionRoverX)
		self.assertEqual(0, roverFour.positionRoverY)

		roverFour.moveRover()
		self.assertEqual(-6, roverFour.positionRoverX)
		self.assertEqual(0, roverFour.positionRoverY)

		roverFour.moveRover()
		self.assertEqual(-7, roverFour.positionRoverX)
		self.assertEqual(0, roverFour.positionRoverY)

		roverFour.moveRover()
		self.assertEqual(-8, roverFour.positionRoverX)
		self.assertEqual(0, roverFour.positionRoverY)

if __name__ == '__main__':
	unittest.main()