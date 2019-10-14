import sys

"""
This class it's like the spaceShip, sending both rovers to Plateau
"""

class SpaceShip:

	def __init__(self, sizePlateauX, sizePlateauY):
		self.__sizePlateauX = int(sizePlateauX)
		self.__sizePlateauY = int(sizePlateauY)
	
	@classmethod
	def setPlateauSize(self):
		__sizePlateauX, __sizePlateauY = input().split()
		return self(__sizePlateauX, __sizePlateauY)

	def confirmPlateauSize(self):
		print('Plateau size confirmed!')

	def sendRovers(self):
		print('Rovers sended!')