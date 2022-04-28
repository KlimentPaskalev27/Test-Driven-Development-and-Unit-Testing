#import unit testing framework
import unittest

class TestSetForOneModule(unittest.TestCase):

    def test_arithmetic_pass(self):
        self.assertEqual(2+2, 4)
    def test_arithmetic_fail(self):
        self.assertEqual(2+2, 3)

unittest.main(argv=['ignored', '-v'], exit=False)

# Each unit test results
#test_arithmetic_fail (__main__.TestSetForOneModule) ... FAIL
#test_arithmetic_pass (__main__.TestSetForOneModule) ... ok

#Overall result
#FAIL: test_arithmetic_fail (__main__.TestSetForOneModule)