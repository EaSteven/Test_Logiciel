import funcs
import unittest

class TestFuncs(unittest.TestCase):

	def test_get_mean(self):
		self.assertEqual(funcs.get_mean([10,12,1,1]),6)
		self.assertEqual(funcs.get_mean([0,1,2,3,4]),2)
		self.assertEqual(funcs.get_mean([-1,-1,-1,-1]),-1)
		self.assertEqual(funcs.get_mean([-1,-2,1,2]),0)
		self.assertEqual(funcs.get_mean([2.5,2.5,2.5,2.5]),2)
	
	def test_min_int(self):
		self.assertEqual(funcs.min_int(0,0),0)
		self.assertEqual(funcs.min_int(-1,0),-1)
		self.assertEqual(funcs.min_int(0,10),0)
		self.assertEqual(funcs.min_int(-1,-2),-2)

	def test_get_mediane(self):
		self.assertEqual(funcs.get_mediane([-1,-5,7,10,12]),7)
		self.assertEqual(funcs.get_mediane([10,1,4,7,8]),7)
		self.assertEqual(funcs.get_mediane([-1,5,6,8]),5.5)
		self.assertEqual(funcs.get_mediane([1,5,4,3,8,9,1,2]),3.5)

	def test_ecart_type(self):
		self.assertEqual(funcs.get_ecart_type([2,7,3,12,9]),3.72)
		self.assertEqual(funcs.get_ecart_type([1,10,15,-10,7,9,5]),7.42)
		self.assertEqual(funcs.get_ecart_type([1,3,5,7,9]),2.83)
		self.assertEqual(funcs.get_ecart_type([0,2,4,6,8,10]),3.42)

	def test_is_Arithm(self):	
		self.assertEqual(funcs.is_Arithm([1,1,1]),True)
		self.assertEqual(funcs.is_Arithm([-1,0,1,2,3]),True)
		self.assertEqual(funcs.is_Arithm([1,2,3,5,6]),False)
		self.assertEqual(funcs.is_Arithm([10,20,30,40,50]),True)

	def test_is_Géo(self):
		self.assertEqual(funcs.is_Géo([1,1,1,1]),True)
		self.assertEqual(funcs.is_Géo([2,4,8,16,32]),True)
		self.assertEqual(funcs.is_Géo([-2,-4,-8,-16,-32]),True)
		self.assertEqual(funcs.is_Géo([3,6,12,15]),False)

	def test_suite_Arithm(self):	
		self.assertEqual(funcs.suite_Arithm([1,1,1],2),(True,[1,1]))
		self.assertEqual(funcs.suite_Arithm([-1,0,1,2,3],4),(True,[4,5,6,7]))
		self.assertEqual(funcs.suite_Arithm([1,2,3,5,6],0),(False,[None]))
		self.assertEqual(funcs.suite_Arithm([10,20,30,40,50],0),(True,[None]))

	def test_suite_Géo(self):
		self.assertEqual(funcs.suite_Géo([1,1,1,1],1),(True,[1]))
		self.assertEqual(funcs.suite_Géo([2,4,8,16,32],-1),(True,[None]))
		self.assertEqual(funcs.suite_Géo([-2,-4,-8,-16,-32],2),(True,[-64,-128]))
		self.assertEqual(funcs.suite_Géo([3,6,12,15],5),(False,[None]))
	
if __name__ == '__main__':
	unittest.main()