import unittest
from fact import fact
import math
  
class TestStringMethods(unittest.TestCase): 
      
    def test_fact(self): 
        self.assertEqual( fact(7), math.factorial(7))
    
    # Returns true if the string splits and matches 
    # the given output. 
    def test_split(self):         
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)
  
if __name__ == '__main__': 
    unittest.main() 