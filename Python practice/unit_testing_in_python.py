import unittest
from calculator import add,divide,double_divide,modulus,multiply,subtract

class TestCalculator(unittest.TestCase):

    def test_add_pass(self):
        result = add(4,4)
        self.assertEquals(8,result)
    
    def test_add_fail(self):
        result = add(10,4)
        self.assertEquals(14,result)

    def test_multiply(self):
        result = multiply(5, 6)
        self.assertEquals(30, result)

    def test_subtract(self):
        result = subtract(5, 6)
        self.assertEquals(-1, result)

    def test_modulus(self):
        result = modulus(9, 2)
        self.assertEquals(1, result)



if __name__ == "__main__":
    unittest.main()