# the aim of the code below is to error again and again 
# in order to facilitate test-driven development of a custom module
# for calculating statistics called snakestats

# the steps of creating snakestats while passing each failed test here is recorded in snakestats.py


# FIRST VERSION - test if module exists and returns 2.0
    # import unittest
    # import snakestats

    # class TestsForSnakeStats(unittest.TestCase):
    #     def test_mean(self):
    #         res = snakestats.mean([1,2,3])
    #         self.assertEqual(res, 2.0)

    # unittest.main(argv=['ignored', '-v'], exit=False)


# SECOND VERSION - add tests to check if module returns mean value of input
import unittest
import snakestats

class TestsForSnakeStats(unittest.TestCase):
    def test_mean_3_values(self):
        res = snakestats.mean([1,2,3])
        self.assertEqual(res, 2.0)

    def test_mean_2_values(self):
        res = snakestats.mean([1,2])
        self.assertEqual(res, 1.5)

unittest.main(argv=['ignored', '-v'], exit=False)



# THIRD VERSION - add getMax and getMaxLast tests
import unittest
import snakestats

class TestsForSnakeStats(unittest.TestCase):
    def test_mean_3_values(self):
        res = snakestats.mean([1,2,3])
        self.assertEqual(res, 2.0)

    def test_mean_2_values(self):
        res = snakestats.mean([1,2])
        self.assertEqual(res, 1.5)

    def test_getMax(self):
        theMax = snakestats.getMax([6,5,4,3,2,1])
        self.assertEqual(theMax, 6)

    def test_getMaxLast(self):
        theMax = snakestats.getMax([6,5,4,3,2,7])
        self.assertEqual(theMax, 7)



unittest.main(argv=['ignored', '-v'], exit=False)
