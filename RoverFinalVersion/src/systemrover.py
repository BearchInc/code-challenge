#!/usr/bin/python

"""
The Rover System
"""

from spaceship import SpaceShip

directions = ['N', 'E', 'S', 'W']

class Rover(SpaceShip):

	def __init__(self, sizePlateauX = 5, sizePlateauY = 5):
		pass

	@classmethod
	def getRoverCleanLocalization(self, roverCommand):
		self.positionRoverX = int(roverCommand[0])
		self.positionRoverY = int(roverCommand[1])
		self.initialDirection = directions.index(roverCommand[2])

	def positionRover(self, commands):

		for command in commands:
			if command == 'R':
				self.rightRotateRover()
			elif command == 'L':
				self.leftRotateRover()
			elif command == 'M':
				self.moveRover()


		directions = ['N', 'E', 'S', 'W'][self.initialDirection]
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

