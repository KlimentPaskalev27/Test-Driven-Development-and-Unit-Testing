# Create own statisticis-processing module to import into snakestats_testing.py
# Each iteration below adds the minimal code to pass a failed unit test in snakestats_testing.py
# The aim so to create the minimum code for a module using test-driven development

# FIRST VERSION code in snakestats_testing.py

    # Iteration 1
        # File "snakestats_testing.py", line 12, in test_mean
        #     res = snakestats.mean([1,2,3])
        # AttributeError: module 'snakestats' has no attribute 'mean'

    # Iteraion 2
        # def mean():
        #     return 0
        
            # TypeError: mean() takes 0 positional arguments but 1 was given 


    # Iteraion 3
        #def mean(values):
        #    return 0

            # self.assertEqual(res, 2.0)
            # AssertionError: 0 != 2.0
        
    # Iteraion 4
    # def mean(values):
        # return 2.0

        # test_mean (__main__.TestsForSnakeStats) ... ok


# SECOND VERSION code in snakestats_testing.py

    # Iteraion 1
        # def mean(values):
        #     return 2.0

            # test_mean_2_values (__main__.TestsForSnakeStats) ... FAIL
            # test_mean_3_values (__main__.TestsForSnakeStats) ... ok
            # AssertionError: 2.0 != 1.5
    
    # Iteraion 2
        # def mean(vals):
        #     sum = vals[0] + vals[1] + vals[2]
        #     return sum / 3

                # test_mean_2_values (__main__.TestsForSnakeStats) ... ERROR
                # test_mean_3_values (__main__.TestsForSnakeStats) ... ok
                # sum = vals[0] + vals[1] + vals[2]
                # IndexError: list index out of range
        
    # Iteraion 3
        # def mean(vals):
        #     sum = 0.0
        #     for i in range(len(vals)):
        #         sum += vals[i]
        #     return sum / len(vals)

                # test_mean_2_values (__main__.TestsForSnakeStats) ... ok
                # test_mean_3_values (__main__.TestsForSnakeStats) ... ok


# THIRD VERSION code in snakestats_testing.py

    # Iteraion 1
        # def mean(vals):
        #     sum = 0.0
        #     for i in range(len(vals)):
        #         sum += vals[i]
        #     return sum / len(vals)

                # test_getMax (__main__.TestsForSnakeStats) ... ERROR
                # test_getMaxLast (__main__.TestsForSnakeStats) ... ERROR
                # test_mean_2_values (__main__.TestsForSnakeStats) ... ok
                # test_mean_3_values (__main__.TestsForSnakeStats) ... ok
                # AttributeError: module 'snakestats' has no attribute 'getMax'


    # Iteraion 2
        # def mean(vals):
        #     sum = 0.0
        #     for i in range(len(vals)):
        #         sum += vals[i]
        #     return sum / len(vals)

        # def getMax(vals):
        #     return vals[0]

            # test_getMax (__main__.TestsForSnakeStats) ... ok
            # test_getMaxLast (__main__.TestsForSnakeStats) ... FAIL  - AssertionError: 6 != 7
            # test_mean_2_values (__main__.TestsForSnakeStats) ... ok
            # test_mean_3_values (__main__.TestsForSnakeStats) ... ok
     

    # Iteraion 3
def mean(vals):
    sum = 0.0
    for i in range(len(vals)):
        sum += vals[i]
    return sum / len(vals)

def getMax(vals):
    maxSeen = 0
    for i in range(len(vals)):
        if vals[i] > maxSeen:
            maxSeen = vals[i]
    return maxSeen

# OK
# test_getMax (__main__.TestsForSnakeStats) ... ok
# test_getMaxLast (__main__.TestsForSnakeStats) ... ok
# test_mean_2_values (__main__.TestsForSnakeStats) ... ok
# test_mean_3_values (__main__.TestsForSnakeStats) ... ok