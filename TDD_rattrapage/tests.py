import functions
import unittest
import math

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
		self.assertEqual(functions.derivee([1,3,7,10,20],1),[2,4,3,10])
		self.assertEqual(functions.derivee([1,1,1,1],2),[0,0,0])
		self.assertEqual(functions.derivee([-1,5,8,-2],1),[6,3,-10])
		
		#Test liste vide
		self.assertEqual(functions.derivee([],1),-1)
		#Test derive en un point
		self.assertEqual(functions.derivee([5],1),-1)

		#Test avec un delta temps = 0 ou inferieur
		self.assertEqual(functions.derivee([5,4,3,2],0),-1)
		self.assertEqual(functions.derivee([5,4,3,2],-1),-1)
		
	
	def test_derivee_seconde(self):
		self.assertEqual(functions.derivee_seconde([1,3,7,10,20],1),[2,-1,7])
		self.assertEqual(functions.derivee_seconde([1,1,1,1],1),[0,0])
		self.assertEqual(functions.derivee_seconde([-1,5,8,-2],1),[-3,-13])
		
		#Test liste vide
		self.assertEqual(functions.derivee_seconde([],1),-1)
		#Test derive en un point
		self.assertEqual(functions.derivee_seconde([5],1),-1)
		#Test derive seconde de 2 point
		self.assertEqual(functions.derivee_seconde([5,9],1),-1)
		
		#Test avec un delta temps = 0 ou inferieur
		self.assertEqual(functions.derivee([5,4,3,2],0),-1)
		self.assertEqual(functions.derivee([5,4,3,2],-1),-1)
		

	def test_approx_derivee(self):

		#Test sinus
		self.assertEqual(functions.approx_derivee(lambda x : math.sin(x),math.pi/2,2),0)
		
		#Test fonction affine
		self.assertEqual(functions.approx_derivee(lambda x :2*x,5,1),2)
		self.assertEqual(functions.approx_derivee(lambda x :2*x + 5,5,1),2)
		
		#Test constante
		self.assertEqual(functions.approx_derivee(lambda x :1,10,2),0)

		#Test exponentielle
		self.assertEqual(functions.approx_derivee(lambda x :math.exp(x),1,2),2.72)

		#Test racine
		self.assertEqual(functions.approx_derivee(lambda x :math.sqrt(x),2,1),0.4)		
		#impossible au point 0
		self.assertEqual(functions.approx_derivee(lambda x :math.sqrt(x),0,1),False)		
		
		#Test quotient
		self.assertEqual(functions.approx_derivee(lambda x :1/x,4,2),-0.06)
		#impossible au point 0
		self.assertEqual(functions.approx_derivee(lambda x :1/x,0,2),False)


if __name__ == '__main__':
	unittest.main()
