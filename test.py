import unittest
from main import add,sub
class test(unittest.TestCase):
  def test_add(self):
    return self.assertEqual(add(2,5),7)
  def test_sub(self):
    return self.assertEqual(sub(3,2),1)
if __name__=="__main__":
  unittest.main()
