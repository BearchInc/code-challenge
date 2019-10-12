#!/usr/bin/python
from spaceshiptest import SpaceShip

import unittest

"""
Rover System | in test please load the file sendrover.py
"""

directions = ['N', 'E', 'S', 'W']

class Rover(SpaceShip):

	def __init__(self, sizePlateauX = 5, sizePlateauY = 5):
		pass

	@classmethod
	def getRoverCleanLocalization(self, roverCommand):
		self.positionRoverX = int(roverCommand[0])
		self.positionRoverY = int(roverCommand[1])
		self.initialDirection = directions.index(roverCommand[2])

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

	def positionRover(self, commands):

		for command in commands:
			if command == 'R':
				self.rightRotateRover()
			elif command == 'L':
				self.leftRotateRover()
			elif command == 'M':
				self.moveRover()


		directions = ['N', 'E', 'S', 'W'][self.initialDirection]
		return f'{self.positionRoverX} {self.positionRoverY} {directions}'

class RoverTest(unittest.TestCase):

	def testMoveRover(self):
		rover = Rover(5, 5)
		rover.getRoverCleanLocalization([1, 2, 'N'])
		self.assertEqual('1 3 N', rover.positionRover('LMLMLMLMM'))

	def testRoverPosition(self):
		rover = Rover(5, 5)
		rover.getRoverCleanLocalization([1, 2, 'N'])

		self.assertEqual(0, rover.initialDirection)
		self.assertEqual(3, rover.leftRotateRover())
		self.assertEqual(0, rover.rightRotateRover())
		self.assertEqual(1, rover.rightRotateRover())
		self.assertEqual(2, rover.rightRotateRover())

	def testMoveRoverFront(self):
		rover = Rover(5, 5)
		rover.getRoverCleanLocalization([1, 2, 'N'])

	def testLocationPositionNorth(self):
		rover = Rover(5, 5)
		rover.getRoverCleanLocalization([1, 2, 'N'])
		rover.positionRover("LMLMLMLMM")

		rover.moveRover()
		self.assertEqual(1, rover.positionRoverX)
		self.assertEqual(4, rover.positionRoverY)

		rover.moveRover()
		self.assertEqual(1, rover.positionRoverX)
		self.assertEqual(5, rover.positionRoverY)

	def testLocationPositionSouth(self):
		rover = Rover(5, 5)
		rover.getRoverCleanLocalization([1, 2, 'S'])
		rover.positionRover("MM")

		rover.moveRover()
		self.assertEqual(1, rover.positionRoverX)
		self.assertEqual(-1, rover.positionRoverY)

		rover.moveRover()
		self.assertEqual(1, rover.positionRoverX)
		self.assertEqual(-2, rover.positionRoverY)

	def testLocationPositionEast(self):
		rover = Rover(5, 5)
		rover.getRoverCleanLocalization([1, 2, 'E'])
		rover.positionRover("MM")

		rover.moveRover()
		self.assertEqual(4, rover.positionRoverX)
		self.assertEqual(2, rover.positionRoverY)

		rover.moveRover()
		self.assertEqual(5, rover.positionRoverX)
		self.assertEqual(2, rover.positionRoverY)		

	def testLocationPositionOest(self):
		rover = Rover(5, 5)
		rover.getRoverCleanLocalization([1, 2, 'W'])
		rover.positionRover("MM")
		
		rover.moveRover()
		self.assertEqual(-2, rover.positionRoverX)
		self.assertEqual(2, rover.positionRoverY)

		rover.moveRover()
		self.assertEqual(-3, rover.positionRoverX)
		self.assertEqual(2, rover.positionRoverY)			

if __name__ == '__main__':
	unittest.main()