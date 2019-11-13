#!/usr/bin/python

from spaceship import SpaceShip

class Rover(SpaceShip):
	"""
	Complete Rover System, CleanCodeBook model used, methods called in cascade.
	"""

	def __init__(self, sizePlateauX = 5, sizePlateauY = 5):
		"""
		Seting Plateau position from the vision of SpaceShip.
		"""
		pass

	@classmethod
	def setRoverCleanLocalization(self, roverCommand):
		"""
		Extended method from class, initializate rover and send commands.
		"""
		self.__directions = ['N', 'E', 'S', 'W']
		self.__positionRoverX = int(roverCommand[0])
		self.__positionRoverY = int(roverCommand[1])
		self.__initialDirection = self.__directions.index(roverCommand[2])

	def __initialHeading(self):
		return self.__initialDirection
	
	def setPositionRover(self, commands):
		"""
		Rover commands'll be read and call another function like on the book CleanCode(cascade).
		"""
		for command in commands:
			if command == 'R':
				self.__rightRotateRover()
			elif command == 'L':
				self.__leftRotateRover()
			elif command == 'M':
				self.__moveRover()

		self.__getHeadingRover()

	def __getHeadingRover(self):
		print(f'{self.__positionRoverX} {self.__positionRoverY} {self.__directions[int(self.__initialHeading())]}')

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