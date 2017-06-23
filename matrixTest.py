import unittest, matrix as m
"""
class initialize(unittest.TestCase):
    def test_initialize(self):
"""

class compare(unittest.TestCase):
    
    def test_equals(self):
        a = m.Matrix([[1, 2], [3, 4]])
        b = m.Matrix([[1, 2], [3, 4]])
        
        self.assertEqual(a,b)
    def test_not_equals(self):
        a = m.Matrix([[1, 3], [2, 4]])
        b = m.Matrix([[1, 2], [3, 4]])
        c = m.Matrix([[1]])
        self.assertNotEqual(a,b)
        self.assertNotEqual(a,c)
class ops(unittest.TestCase):
    def test_sum(self):
        a = m.Matrix([[1, 3], [2, 4]])
        b = m.Matrix([[1, 2], [3, 4]])
        res = m.Matrix([[2,5],[5,8]])
        self.assertEqual(a+b,res)
    def test_scal_mul(self):
        a = m.Matrix([[1, 3], [2, 4]])
        res = m.Matrix([[4,12],[8,16]])
        self.assertEqual(a*4,res)
    def test_matmul(self):
        a = m.Matrix([[1, 3], [2, 4]])
        i = m.Matrix([[1,0],[0,1]])
        self.assertEqual(a@i,a)
class checkBadInput(unittest.TestCase):
    def test_badlist_in_constructor(self):
        self.assertRaises(ValueError,  m.Matrix,[[1],[8,5],[78,5]])

class checkSums(unittest.TestCase):
    def test_sum_by_row(self):
        self.assertEqual(m.Matrix([[1, 2], [3, 4]]).sum_by_row(), [3,7])
    def test_sum_by_column(self):
        self.assertEqual(m.Matrix([[1, 2], [3, 4]]).sum_by_column(), [4,6])
        
class squareConstructor(unittest.TestCase):
    def test_constructor_makes_identity(self):
        self.assertEqual(m.SquareMatrix(2), m.Matrix([[1,0],[0,1]]))
if __name__ == '__main__': unittest.main()
