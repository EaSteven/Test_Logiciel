import functions
import unittest


class Test(unittest.TestCase):
	def test_mirror(self):

		self.assertEqual(functions.mirror("azertyuiop",3),"azerreza")
		self.assertEqual(functions.mirror("AZERTYUIOP",0),"AA")
		self.assertEqual(functions.mirror("azertyuiop",9),"azertyuioppoiuytreza")
		
		#Test entier > à la taille de la string en entrée
		self.assertEqual(functions.mirror("azertyuiop",15),-1)
		
		#Test entier negatif
		self.assertEqual(functions.mirror("azertyuiop",-1),-1)

		#Test float
		self.assertEqual(functions.mirror("azertyuiop",1.0),-1)

	def test_derivee(self):
		self.assertEqual(functions.derivee([1,3,7,10,20]),[2,4,3,10])
		self.assertEqual(functions.derivee([1,1,1,1]),[0,0,0])
		self.assertEqual(functions.derivee([-1,5,8,-2]),[6,3,-10])
		
		#Test liste vide
		self.assertEqual(functions.derivee([]),-1)
		#Test derive en un point
		self.assertEqual(functions.derivee([5]),-1)
		
	
	def test_derivee_seconde(self):
		self.assertEqual(functions.derivee_seconde([1,3,7,10,20]),[2,-1,7])
		self.assertEqual(functions.derivee_seconde([1,1,1,1]),[0,0])
		self.assertEqual(functions.derivee_seconde([-1,5,8,-2]),[-3,-13])
		
		#Test liste vide
		self.assertEqual(functions.derivee_seconde([]),-1)
		#Test derive en un point
		self.assertEqual(functions.derivee_seconde([5]),-1)
		#Test derive seconde de 2 point
		self.assertEqual(functions.derivee_seconde([5,9]),-1)
		
		


if __name__ == '__main__':
	unittest.main()
