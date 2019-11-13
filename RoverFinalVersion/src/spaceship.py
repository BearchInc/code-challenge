class SpaceShip:
	"""
	SpaceShip who have vision from plateau.
	"""

	def __init__(self, sizePlateauX, sizePlateauY):
		self.__sizePlateauX = int(sizePlateauX)
		self.__sizePlateauY = int(sizePlateauY)
	
	@classmethod
	def setPlateauSize(self):
		"""
		Extended method from class SpaceShip setting
		"""
		__sizePlateauX, __sizePlateauY = input().split()
		return self(__sizePlateauX, __sizePlateauY)
