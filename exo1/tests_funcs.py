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


if __name__ == '__main__':
	unittest.main()