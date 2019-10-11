import sys
import unittest

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

class SpaceShipTest(unittest.TestCase):

	def testSize(self):
		plateauOne = SpaceShip(5, 5)
		plateauOne.confirmPlateauSize()
		plateauOne.sendRovers()

		plateauTwo = SpaceShip.getPlateauSize()
		plateauTwo.confirmPlateauSize()
		plateauTwo.sendRovers()

if __name__ == '__main__':
	unittest.main()
