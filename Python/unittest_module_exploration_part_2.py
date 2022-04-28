#import unit testing framework - https://docs.python.org/3/library/unittest.html
import unittest

#used for tests eleven and twelve 
def doNotReturn():
        x = 10

#class that holds all tests
class TestSetForOneModule(unittest.TestCase):

    def test_arithmetic_pass(self):
        self.assertEqual(2+2, 4)
    #test_arithmetic_fail (__main__.TestSetForOneModule) ... FAIL

    def test_arithmetic_fail(self):
        self.assertEqual(2+2, 3)
    #test_arithmetic_pass (__main__.TestSetForOneModule) ... ok


    # unittest module requires tests to be named with "test" in front
    def not_a_test(self):
        self.assertEqual(10,12)
    # this returns - Ran 0 tests in 0.000s

    def test_one(self):
        self.assertEqual(10,12)
    # this returns - Ran 1 test in 0.001s
    # test_one (__main__.TestSetForOneModule) ... FAIL

    def test_two(self):
        self.assertEqual(10,10)
    # test_two (__main__.TestSetForOneModule) ... ok

    def test_three(self):
        self.assertTrue(1)
    # test_three (__main__.TestSetForOneModule) ... ok

    def test_four(self):
        self.assertTrue(10 - 5)
    # test_four (__main__.TestSetForOneModule) ... ok

    def test_five(self):
        self.assertTrue(2==4)
    # test_five (__main__.TestSetForOneModule) ... FAIL

    def test_six(self):
        self.assertFalse(2==4)
    # test_six (__main__.TestSetForOneModule) ... ok

    def test_seven(self):
        a = 10
        b = a
        self.assertIs(a, b)
    # test_seven (__main__.TestSetForOneModule) ... ok

    def test_eight(self):
        a = 10
        b = 12
        self.assertIs(a, b)
    # test_eight (__main__.TestSetForOneModule) ... FAIL

    def test_nine(self):
        a = 10
        b = 12
        self.assertIsNot(a, b)
    # test_nine (__main__.TestSetForOneModule) ... ok

    def test_ten(self):
        self.assertIsNone(a)
    # test_ten (__main__.TestSetForOneModule) ... ERROR

    
    def test_eleven(self):
        self.assertIsNone(doNotReturn())
    # test_eleven (__main__.TestSetForOneModule) ... ok

    def test_twelve(self):
        self.assertIsNotNone(doNotReturn())
    # test_twelve (__main__.TestSetForOneModule) ... FAIL

    def test_13(self):
        a = [1,2,3,5,6,7]
        self.assertIn(4, a)
    # test_13 (__main__.TestSetForOneModule) ... FAIL 

    def test_14(self):
        a = [1,2,3,5,6,7]
        self.assertNotIn(7, a)
    # test_13 (__main__.TestSetForOneModule) ... FAIL

    def test_15(self):
        a = [1,2,3,5,6,7]
        self.assertIsInstance(a, list)
    # test_15 (__main__.TestSetForOneModule) ... ok

    def test_16(self):
        a = 1
        self.assertIsInstance(a, list)
    # test_16 (__main__.TestSetForOneModule) ... FAIL

    def test_17(self):
        a = 1
        self.assertNotIsInstance(a, int)
    # test_17 (__main__.TestSetForOneModule) ... FAIL


unittest.main(argv=['ignored', '-v'], exit=False)