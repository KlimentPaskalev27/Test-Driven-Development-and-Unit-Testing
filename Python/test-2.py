#import unit testing framework
import unittest

class TestSetForOneModule(unittest.TestCase):

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





unittest.main(argv=['ignored', '-v'], exit=False)

# Each unit test results
#test_arithmetic_fail (__main__.TestSetForOneModule) ... FAIL
#test_arithmetic_pass (__main__.TestSetForOneModule) ... ok

#Overall result
#FAIL: test_arithmetic_fail (__main__.TestSetForOneModule)