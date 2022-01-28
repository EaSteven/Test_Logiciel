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

if __name__ == '__main__':
	unittest.main()
