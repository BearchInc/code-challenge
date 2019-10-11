import sys

"""
This class it's like the spaceShip, sending both rovers to Plateau
"""

class SpaceShip:

	def __init__(self, sizePlateauX, sizePlateauY):
		self.sizePlateauX = int(sizePlateauX)
		self.sizePlateauY = int(sizePlateauY)
	
	@classmethod
	def getPlateauSize(self):
		sizePlateauX, sizePlateauY = input().split()
		return self(sizePlateauX, sizePlateauY)

	def confirmPlateauSize(self):
		print('Plateau size confirmed!')

	def sendRovers(self):
		print('Rovers sended!')