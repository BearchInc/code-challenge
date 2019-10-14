import sys
import unittest

class SpaceShip:

	def __init__(self, sizePlateauX, sizePlateauY):
		self.__sizePlateauX = int(sizePlateauX)
		self.__sizePlateauY = int(sizePlateauY)
	
	@classmethod
	def getPlateauSize(self):
		__sizePlateauX, __sizePlateauY = input().split()
		return self(__sizePlateauX, __sizePlateauY)

	def confirmPlateauSize(self):
		print('Plateau size confirmed!')

	def sendRovers(self):
		print('Rovers sended!')

class SpaceShipTest(unittest.TestCase):

	def testSize(self):
		plateauOne = SpaceShip(5, 5)
		plateauOne.confirmPlateauSize()
		plateauOne.sendRovers()

if __name__ == '__main__':
	unittest.main()
