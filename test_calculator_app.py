import unittest
import calculator


class TestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(calculator.add(1,2),3)

    def test2(self):
        self.assertEqual(calculator.sub(2,1),1)

    def test3(self):
        self.assertEqual(calculator.mul(2,2),4)

    def test4(self):
        self.assertEqual(calculator.div(4,2),2)

    def test5(self):
        self.assertEqual(calculator.div(4,0),0)

    def test6(self):
        self.assertEqual(calculator.sub(4,'2'),2)

    def test7(self):
        self.assertEqual(calculator.mul('40','0'),0)

    def test8(self):
        self.assertEqual(calculator.add('cheese','burger'),1)

if __name__ == '__main__':
    unittest.main(verbosity = 2)
