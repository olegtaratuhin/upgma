"""
This file contains random generator for tables.
"""

import random


class RandomGenerator(object):
    """
    Class for generating random tables (properly formatted) and saving them
    for testing purposes.
    """

    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)

    def generate(self, number_of_tests, min_test_size=5, max_test_size=1000):
        for i in range(number_of_tests):
            test_size = random.randint(min_test_size, max_test_size)

            labels = ['L' + str(i) for i in range(test_size)]
            matrix = [['0' for _ in range(test_size)] for _ in range(test_size)]
            for j in range(test_size):
                for k in range(j + 1, test_size):
                    matrix[j][k] = str(random.random())

            with open("random_tests/test_" + str(i) + ".txt", "w") as f:
                f.write(' '.join(labels))
                f.write('\n')
                for l in range(test_size):
                    f.write(labels[l])
                    f.write(' ')
                    f.write(' '.join(matrix[l]))
                    f.write('\n')


if __name__ == "__main__":
    g = RandomGenerator()
    g.generate(10)
