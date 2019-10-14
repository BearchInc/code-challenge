#!/usr/bin/python

"""
The Rover System
"""

from spaceship import SpaceShip

class Rover(SpaceShip):

	def __init__(self, sizePlateauX = 5, sizePlateauY = 5):
		pass

	@classmethod
	def setRoverCleanLocalization(self, roverCommand):
		self.__directions = ['N', 'E', 'S', 'W']
		self.__positionRoverX = int(roverCommand[0])
		self.__positionRoverY = int(roverCommand[1])
		self.__initialDirection = self.__directions.index(roverCommand[2])

	def __initialHeading(self):
		return self.__initialDirection
	
	def setPositionRover(self, commands):
		for command in commands:
			if command == 'R':
				self.__rightRotateRover()
			elif command == 'L':
				self.__leftRotateRover()
			elif command == 'M':
				self.__moveRover()

		self.__getHeadingRover()

	def __moveRover(self):
		if(self.__checkNorth()):
			self.__positionRoverY += 1

		if(self.__checkSouth()): 
			self.__positionRoverY -= 1

		if(self.__checkEast()): 
			self.__positionRoverX += 1

		if(self.__checkWeast()): 
			self.__positionRoverX -= 1

		return True

	def __checkNorth(self):
		return self.__initialHeading() == 0

	def __checkSouth(self):
		return self.__initialHeading() == 2

	def __checkEast(self):
		return self.__initialHeading() == 1

	def __checkWeast(self):
		return self.__initialHeading() == 3

	def __rightRotateRover(self):
		self.__initialDirection = 0 if self.__initialHeading() == 3 else self.__initialHeading() + 1

	def __leftRotateRover(self):
		self.__initialDirection = 3 if self.__initialHeading() == 0 else self.__initialHeading() - 1

	def __getHeadingRover(self):
		print(f'{self.__positionRoverX} {self.__positionRoverY} {self.__directions[int(self.__initialHeading())]}')